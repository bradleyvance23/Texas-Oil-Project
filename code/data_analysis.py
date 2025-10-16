import pandas as pd
import statsmodels.api as sm
from clean import process_csvs, csv_info

yearly_dataframes = process_csvs(csv_info)

df_price = yearly_dataframes[0].rename(columns={'Average': 'Price_per_Barrel'})
df_production = yearly_dataframes[1].rename(columns={'Average': 'Production_Barrels'})
df_wells = yearly_dataframes[2].rename(columns={'Average': 'Oil_Well_Count'})
df_gdp = yearly_dataframes[3].rename(columns={'Average': 'Texas_GDP'})

dfs = [df_price, df_production, df_wells, df_gdp]
df = dfs[0]
for other_df in dfs[1:]:
    df = df.merge(other_df, on='Year', how='inner')

print(df.info())
print(df.describe())

y = df['Price_per_Barrel']
X = df[['Production_Barrels', 'Oil_Well_Count', 'Texas_GDP']]
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print(model.summary())
df['Predicted_Price'] = model.predict(X)

print('\n' + '='*60 + '\n')

with open("artifacts/regression_summary.html", "w") as f:
    f.write(model.summary().as_html())

for var in ['Production_Barrels', 'Oil_Well_Count', 'Texas_GDP']:
    Z = df[[var]]
    Z = sm.add_constant(Z)
    model = sm.OLS(y, Z).fit()
    print(f'Regression: Price_per_Barrel ~ {var}')
    print(model.summary())
    print('\n' + '='*60 + '\n')
