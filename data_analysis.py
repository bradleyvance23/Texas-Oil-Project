import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

df.info()
df.describe()

y = df['Price_per_Barrel']

X = ['Production_Barrels', 'Oil_Well_Count', 'Texas_GDP']

X = sm.add_constant(df[X])

model = sm.OLS(y, X).fit()
print(model.summary())

print('\n' + '='*60 + '\n')

for var in ['Production_Barrels', 'Oil_Well_Count', 'Texas_GDP']:
    Z = df[[var]]
    Z = sm.add_constant(Z)
    model = sm.OLS(y, Z).fit()
    print(f'Regression: Price_per_Barrel ~ {var}')
    print(model.summary())
    print('\n' + '='*60 + '\n')