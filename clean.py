import pandas as pd

def dataframes_and_yearly_averages(csv_path, year = 'Year', value = 'Value'):

    df = pd.read_csv(csv_path)
    df[year] = pd.