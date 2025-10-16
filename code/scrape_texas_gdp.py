import requests
import os 
import csv
from dotenv import load_dotenv

def main():

	FRED_API_KEY = "c4dd8f412e6a4f35c90c07a8c0292de3"
	
	SERIES_ID = "TXPETCOALMANNGSP"
	URL = "https://api.stlouisfed.org/fred/series/observations"

	params = {
		"series_id": SERIES_ID,
		"api_key": FRED_API_KEY,
		"file_type": "json"
	}

	def get_fred_gdp(url, params):
		response = requests.get(url, params=params)
		response.raise_for_status()
		
		return response.json()

	fred_json = get_fred_gdp(URL,params)

	def parse_fred_data(json_data):
		rows = []
		for obs in json_data.get("observations", []):
			date = obs.get("date")
			value = obs.get("value")
			if value == ".":
				continue
			rows.append({ 
				"Year":date,
				"GDP (Millions of Dollars)":value 
			})
		return rows 

	def write_gdp_csv(data, filename="TX_OIL_GDP.csv"):
		fieldnames = ("Year", "GDP (Millions of Dollars)")

		with open(filename, "w", newline="") as f:
			writer = csv.DictWriter(f, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerows(data)

	texas_oil_gdp = parse_fred_data(fred_json)
	write_gdp_csv(texas_oil_gdp)

if __name__ == "__main__":
    main()