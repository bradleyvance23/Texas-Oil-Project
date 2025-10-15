import requests
import os 
import csv
from dotenv import load_dotenv

load_dotenv()
FRED_API_KEY = os.getenv("FRED_API_KEY")
if not FRED_API_KEY:
	raise RuntimeError("FRED_API_KEY not set. Create a .env file with FRED_API_KEY=your_key")

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