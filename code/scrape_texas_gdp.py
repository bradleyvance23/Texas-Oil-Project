import requests
from bs4 import BeautifulSoup 
import csv

SERIES_ID = "TXPETCOALMANNGSP"
URL = "https://api.stlouisfed.org/fred/series/observations"

def get_fred_gdp(url, params):
	response = requests.get(url, params=prarams)
	response.raise_for_status()
	return response.json()
