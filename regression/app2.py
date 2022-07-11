import numpy as np
import statsmodels.api as sm
import pandas as pd

df = pd.read_csv('california_housing.csv')

model = sm.OLS(df['price'],df[['year','rooms','bedrooms']]).fit()

print(model.summary())
a=model.predict([20,1000,200])
print(a)