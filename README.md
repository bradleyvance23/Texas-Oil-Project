# Texas-Oil-Project
Oil Production Midterm Project

## Project Overview
This project investigates how **Texas oil prices** have impacted **Texas oil production** - measured by well counts and barrel production.  
We scarped data on our individual variables to create a combined dataset to study production trends, economic cycles and potential casual relationships between production activity and the broader economic preformance. 
We utilized regression analysis and a time-series technique to identify whether increases in oil output or well counts are associated with changes in oil prices.

### Research Questions
* How have Texas oil well counts and production levels evolved over time? 
* Is there a measurable relationship between oil production and oil prices?
* How does oil productivty or activity correlate with Texas GDP?  

## Data Sources
- **Well Counts** | Annual Texas oil well counts since 1935 | [Texas Railroad Commision](https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/production-data/historical-production-data/crude-oil-production-and-well-counts-since-1935/)
- **Oil Production (Barrels)** | Monthly field production of crude oil in Texas | [US Energy Information Administration](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=MCRFPTX2&f=M)
- **Texas GDP** | Annual State GDP | [FRED - NGSP](https://fred.stlouisfed.org/graph/?g=hz8p)
- **Oil Prices** | Texas Crude Oil First Purchase Price (dollars per barrel) | [US Energy Information Administration](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=F003048__3&f=M)    
### Data Collection 
All data is stored in the '/code' folder. We cleaned and merged the datasets to ensure consistent:
- Units 
- Observation Frequency
- Date Alignment 

## Methodology
We estimate the relationships through a regression model(s)
## Regression Results 

## ASnalysis/ Discussion

### Limitations 
- Data frequency 
-  
### Next Steps (extensions)
- Compare Texas to another major oil-producing state (i.e. New Mexico or North Dakota)
- 

## Reproduction
1. Scrape all data in one .py file
2. clean data into dataframe 
3. use dataframe to run an analysis 
