import os
import pandas as pd
import statsmodels.api as sm
import main_scrape_file

main_scrape_file.run_all_scraping()

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_files = {
    "prices": os.path.join(script_dir, '../artifacts/monthly_oil_prices.csv'),
    "production": os.path.join(script_dir, '../artifacts/monthly_oil_production.csv'),
    "wells": os.path.join(script_dir, '../artifacts/texas_well_counts.csv'),
}
def melt_monthly_csv(file_path):
    months = ['January','February','March','April','May','June',
              'July','August','September','October','November','December']
    df = pd.read_csv(file_path)
    df_long = df.melt(id_vars=['Year'], value_vars=months,
                      var_name='Month', value_name='Value')
    df_long['Date'] = pd.to_datetime(df_long['Year'].astype(str) + '-' + df_long['Month'] + '-01')
    return df_long[['Date', 'Value']]

price_df = melt_monthly_csv(csv_files["prices"]).rename(columns={'Value': 'Price_per_Barrel'})
prod_df = melt_monthly_csv(csv_files["production"]).rename(columns={'Value': 'Production_Barrels'})
well_df = pd.read_csv(csv_files["wells"])

if 'Year' in well_df.columns:
    well_df['Date'] = pd.to_datetime(well_df['Year'].astype(str) + '-01-01')
else:
    raise KeyError("Expected 'Year' column in texas_well_counts.csv")

prod_merge = pd.merge(price_df, prod_df, on='Date', how='inner').dropna()
well_merge = pd.merge(price_df, well_df, on='Date', how='inner').dropna()

def run_regression(df, y_col, x_col, name):
    X = sm.add_constant(df[[x_col]])
    y = df[y_col]
    model = sm.OLS(y, X).fit()

    output_dir = os.path.join(script_dir, '../artifacts/')
    os.makedirs(output_dir, exist_ok=True)
    summary_path = os.path.join(output_dir, f'regression_{name}.txt')
    coeff_path = os.path.join(output_dir, f'regression_{name}_coefficients.csv')

    with open(summary_path, 'w') as f:
        f.write(model.summary().as_text())

    pd.DataFrame({
        'Variable': model.params.index,
        'Coefficient': model.params.values,
        'P_value': model.pvalues.values
    }).to_csv(coeff_path, index=False)

    print(f"✅ Regression complete: {name}")
    print(f"   Summary: {summary_path}")
    print(f"   Coefficients: {coeff_path}")
    print(model.summary())
  

run_regression(prod_merge, "Production_Barrels", "Price_per_Barrel", "production_vs_price")
run_regression(well_merge, "Well_Count", "Price_per_Barrel", "well_count_vs_price")