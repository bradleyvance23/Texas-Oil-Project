import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_files = [
    os.path.join(script_dir, '../artifacts/monthly_oil_prices.csv'),
    os.path.join(script_dir, '../artifacts/monthly_oil_production.csv'),
    os.path.join(script_dir, '../artifacts/texas_well_counts.csv'),
    os.path.join(script_dir, '../artifacts/TX_OIL_GDP.csv'),
]

csv_info = [
    {'file': csv_files[0], 'type': 'monthly', 'month_cols': ['January','February','March','April','May','June','July','August','September','October','November','December']},
    {'file': csv_files[1], 'type': 'monthly', 'month_cols': ['January','February','March','April','May','June','July','August','September','October','November','December']},
    {'file': csv_files[2], 'type': 'yearly', 'value_col': 'Well_Count'},
    {'file': csv_files[3], 'type': 'yearly', 'value_col': 'GDP (Millions of Dollars)'}
]

def process_csvs(csv_info):
    yearly_dfs = []
    
    for info in csv_info:
        df = pd.read_csv(info['file'])
        
        if info['type'] == 'monthly':
            df['Average'] = df[info['month_cols']].mean(axis=1)
            yearly_avg = df[['Year', 'Average']]
        elif info['type'] == 'yearly':
            yearly_avg = df[['Year', info['value_col']]].rename(columns={info['value_col']: 'Average'})
        else:
            raise ValueError("CSV type must be 'monthly' or 'yearly'")
        
        yearly_dfs.append(yearly_avg)
    
    return yearly_dfs

yearly_dataframes = process_csvs(csv_info)