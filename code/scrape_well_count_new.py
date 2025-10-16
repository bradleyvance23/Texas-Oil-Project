import os
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.join(script_dir, '../artifacts')
    os.makedirs(artifacts_dir, exist_ok=True)

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

        df = pd.read_html(str(table))[0]
        df.columns = [col.strip() for col in df.columns]

        year_col = [col for col in df.columns if "Year" in col][0]
        wells_col = [col for col in df.columns if "Number of Producing Wells" in col][0]

        well_counts = []
        for _, row in df.iterrows():
            try:
                year = int(row[year_col])
                well_count = int(str(row[wells_col]).replace(",", ""))
                well_counts.append({"Year": year, "Well_Count": well_count})
            except (ValueError, TypeError):
                continue  
        return well_counts

    def save_well_counts(well_counts, filename="texas_well_counts.csv"):
        """Save the well counts to CSV file in artifacts folder."""
        filepath = os.path.join(artifacts_dir, filename)
        fieldnames = ["Year", "Well_Count"]

        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(well_counts)
        print(f"Data saved to {filepath}")

    data = request_raw_well_data()
    save_well_counts(data)
    
if __name__ == "__main__":
    main()
