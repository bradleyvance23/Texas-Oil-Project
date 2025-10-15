import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_files = [
    os.path.join(script_dir, '../artifacts/monthly_oil_prices.csv'),
    os.path.join(script_dir, '../artifacts/texas_well_counts.csv'),
    os.path.join(script_dir, '../artifacts/monthly_oil_production.csv'),
    os.path.join(script_dir, '../artifacts/TX_OIL_GDP.csv'),
]

def dataframes_and_averages(csv_paths, year_col='Year', value_col='Value', monthly_sep='-'):

    yearly_dfs = []
    
    for path in csv_paths:
        df = pd.read_csv(path)
        
        if monthly_sep in str(df[year_col].iloc[0]):
            df['Year'] = df[year_col].str.split(monthly_sep).str[0].astype(int)
            yearly_avg = df.groupby('Year')[value_col].mean().reset_index()
            yearly_avg.rename(columns={value_col: 'Average'}, inplace=True)
        else:
            df['Year'] = df[year_col].astype(int)
            yearly_avg = df[[year_col, value_col]].rename(columns={year_col: 'Year', value_col: 'Average'})
        
        yearly_dfs.append(yearly_avg)
    
    return yearly_dfs

yearly_dataframes = dataframes_and_averages(csv_files, year_col='Date', value_col='Production')

for df in yearly_dataframes:
    print(df.head())