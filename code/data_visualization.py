import os
import matplotlib.pyplot as plt
from data_analysis import df

script_dir = os.path.dirname(os.path.abspath(__file__))
path_1 = os.path.join(script_dir, '../artifacts/texas_oil_price_actual_vs_predicted.png')
path_2 = os.path.join(script_dir, '../artifacts/texas_oil_price_time_series.png')

plt.figure(figsize=(10,6))
plt.plot(df['Year'], df['Price_per_Barrel'], marker='o', linestyle='-', label='Actual Price', color='blue')
plt.plot(df['Year'], df['Predicted_Price'], marker='x', linestyle='--', label='Predicted Price', color='red')
plt.xlabel('Year')
plt.ylabel('Price per Barrel')
plt.title('Texas Oil Price: Actual vs Predicted')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(path_1, dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(df['Year'], df['Price_per_Barrel'], marker='o', label='Actual', color='blue')
plt.plot(df['Year'], df['Predicted_Price'], marker='x', label='Predicted', color='red')
plt.xlabel('Year')
plt.ylabel('Price per Barrel ($)')
plt.title('Time Series: Actual vs Predicted Price per Barrel')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(path_2, dpi=300, bbox_inches='tight')
plt.show()
