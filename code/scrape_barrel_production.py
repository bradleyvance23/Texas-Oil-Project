import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=MCRFPTX2&f=M"

def main():

    def get_soup(url):
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            print(f"Error: {response.status_code}")
            return None
        
    def scrape_monthly_data(soup):
        data = []
        rows = soup.find_all("tr")
        
        for row in rows:
            year_tag = row.find("td", class_="B4")
            if not year_tag:
                continue
            year = year_tag.get_text(strip=True)[-4:]
            if not year.isdigit():
                continue
            
            month_tags = row.find_all("td", class_="B3")
            month_values = [td.get_text(strip=True).replace(",", "") for td in month_tags]
            month_values = [float(v) if v else None for v in month_values]

            while len(month_values) < 12:
                month_values.append(None)

            data.append({
                "Year": int(year),
                "January": month_values[0],
                "February": month_values[1],
                "March": month_values[2],
                "April": month_values[3],
                "May": month_values[4],
                "June": month_values[5],
                "July": month_values[6],
                "August": month_values[7],
                "September": month_values[8],
                "October": month_values[9],
                "November": month_values[10],
                "December": month_values[11],
            })
        return data 

    def save_to_csv(data, filename="monthly_oil_production.csv"):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    soup = get_soup(url)
    if soup:
        monthly_data = scrape_monthly_data(soup)
        save_to_csv(monthly_data)

if __name__ == "__main__":
    main()