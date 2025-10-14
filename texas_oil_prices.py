import requests
from bs4 import BeautifulSoup
import os
import csv

url = "https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=F003048__3&f=M"

def get_soup(url):

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    return soup

def year(soup):

    b4_tag = soup.find_all("td", class_="B4")
    years = []
    for i in b4_tag:
        text = i.get_text(strip=True)
        year_str = text[-4:]
        if year_str.isdigit():
            years.append(text)

    return years

soup = get_soup(url)
# print(year(soup))

def monthly_oil_prices(soup):

    b3_tag = soup.find_all("td", class_="B3")
    oil_prices = []
    for i in b3_tag:
        text = i.get_text(strip=True)
        oil_str = text[-3:]
        if oil_str.isdigit():
            oil_prices.append(text)

    return oil_prices

print(monthly_oil_prices(soup))