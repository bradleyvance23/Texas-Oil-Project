import scrape_barrel_production
import scrape_texas_gdp
import scrape_well_count_new
import texas_oil_prices

def run_all_scraping():
    print("Running scraping files\n")

    scrape_barrel_production.main()
    scrape_texas_gdp.main()
    scrape_well_count_new.main()
    texas_oil_prices.main()

    print("\nScraping complete")

if __name__ == "__main__":
    run_all_scraping()
