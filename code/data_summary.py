import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from clean import process_csvs, csv_info

"""Import and merge data from clean.py"""
yearly_dfs = process_csvs(csv_info)

merged_df = yearly_dfs[0].merge(yearly_dfs[1], on="Year", suffixes=("_price", "_production"))
merged_df = merged_df.merge(yearly_dfs[2], on="Year")
merged_df = merged_df.merge(yearly_dfs[3], on="Year", suffixes=("_wellcount", "_gdp"))

merged_df.columns = ["Year", "Oil_Price", "Oil_Production", "Well_Count", "GDP"]

"""Save summary statistics"""
summary = merged_df.describe()
summary.to_csv("artifacts/summary_statistics.csv")

"""Create a line chart for all the variables"""
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=merged_df, x="Year", y="Oil_Price", label="Oil Price ($/barrel)")
sns.lineplot(data=merged_df, x="Year", y="Oil_Production", label="Oil Production")
sns.lineplot(data=merged_df, x="Year", y="Well_Count", label="Well Count")
sns.lineplot(data=merged_df, x="Year", y="GDP", label="Oil GDP (Millions)")
plt.title("Oil Price, Production, Well Count, and GDP Over Time")
plt.xlabel("Year")
plt.ylabel("Values")
plt.legend()
plt.tight_layout()
plt.savefig("artifacts/line_graph_oil_trends.png", dpi=300)


"""Dual-axis Price vs Production"""
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('Oil Price ($/barrel)', color=color)
ax1.plot(merged_df['Year'], merged_df['Oil_Price'], color=color, label='Oil Price')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Oil Production', color=color)
ax2.plot(merged_df['Year'], merged_df['Oil_Production'], color=color, label='Oil Production')
ax2.tick_params(axis='y', labelcolor=color)

plt.title("Oil Price vs Oil Production Over Time")
fig.tight_layout()
plt.savefig("artifacts/dual_axis_price_vs_production.png", dpi=300)

