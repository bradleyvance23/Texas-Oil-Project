import requests
from bs4 import BeautifulSoup 
import csv
from dotenv import load_dotenv

load_dotenv()
FRED_API_KEY = os.getenv("FRED_API_KEY")
if not FRED_API_KEY:
	raise RuntimeError("FRED_API_KEY not set. Create a .env file with FRED_API_KEY=your_key")

SERIES_ID = "TXPETCOALMANNGSP"
URL = "https://api.stlouisfed.org/fred/series/observations"

def get_fred_gdp(url, params):
	response = requests.get(url, params=prarams)
	response.raise_for_status()
	
	return response.json()

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
