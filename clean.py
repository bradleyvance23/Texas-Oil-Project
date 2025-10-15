import pandas as pd

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