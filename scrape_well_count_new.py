import os
import csv
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

def request_raw_well_data():
    """
    Request Texas RRC crude oil production data and extract
    'Year' and 'Number of Producing Wells' into a dictionary.
    """
    url = "https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/production-data/historical-production-data/crude-oil-production-and-well-counts-since-1935/"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    # Read the table into a DataFrame
    df = pd.read_html(str(table))[0]
    df.columns = [col.strip() for col in df.columns]

    # Identify columns
    year_col = [col for col in df.columns if "Year" in col][0]
    wells_col = [col for col in df.columns if "Number of Producing Wells" in col][0]

    # Build list of dicts (for easy writing to CSV)
    well_counts = []
    for _, row in df.iterrows():
        try:
            year = int(row[year_col])
            well_count = int(str(row[wells_col]).replace(",", ""))
            well_counts.append({"Year": year, "Well_Count": well_count})
        except (ValueError, TypeError):
            continue  # skip invalid rows
    print("data saved")
    return well_counts



