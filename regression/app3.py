from pyexpat import model
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_table('ni.txt')
df = df.dropna()

def 함수(x, a, b, c):
    return a*x + b*x**2 + c

opt, cov = curve_fit(함수,df['age'],df['income'])
a,b,c = opt

#x = np.array([1,2,3,4,5,6])
#plt.plot(x,함수(x,a,b,c))
#plt.scatter(df['age'],df['income'])
#plt.show()

import statsmodels.api as sm

x1 = np.column_stack([df['age'],df['age']**2]) 
model = sm.OLS(df['income'],x1).fit()
print(model.summary())

#curve_fit(함수,x,y)
#plt.scatter(df['age'], df['income'])
#plt.show()
#overfitting 너무 다차원으로 하면(curve) 너무나도 적합해짐