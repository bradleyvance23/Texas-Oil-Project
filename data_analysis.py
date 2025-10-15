import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

df.info()
df.describe()

y = ['Price_per_Barrel']

X = ['Production_Barrels', 'Oil_Well_Count', 'Texas_GDP']

X = sm.add_constant(df[X])

model = sm.OLS(df[y], X).fit()
print(model.summary())