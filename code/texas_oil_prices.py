import requests
from bs4 import BeautifulSoup
import os
import csv

def main():

    url = "https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=F003048__3&f=M"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.join(script_dir, '../artifacts')

    def get_soup(url):

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        return soup

    soup = get_soup(url)

    def monthly_data_per_year(soup):
        data = []
        rows = soup.find_all("tr")

        for i in rows:
            year_tag = i.find("td", class_="B4")
            if not year_tag:
                continue

            year_text = year_tag.get_text(strip = True)[-4:]
            if not year_text.isdigit():
                continue

            month_tag = i.find_all("td", class_="B3")
            month_text = [w.get_text(strip = True) for w in month_tag]

            while len(month_text) < 12:
                month_text.append("")
            
            data.append({
                "Year" : year_text,
                "January" : month_text[0],
                "February" : month_text[1],
                "March" : month_text[2],
                "April" : month_text[3],
                "May" : month_text[4],
                "June" : month_text[5],
                "July" : month_text[6],
                "August" : month_text[7],
                "September" : month_text[8],
                "October" : month_text[9],
                "November" : month_text[10],
                "December" : month_text[11],
            })
        
        return data

    def csv_writer(data, filename="monthly_oil_prices.csv"):
        
        filepath = os.path.join(artifacts_dir, filename)
        fieldnames=["Year", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    yearly_data = monthly_data_per_year(soup)
    csv_writer(yearly_data)

if __name__ == "__main__":
    main()
