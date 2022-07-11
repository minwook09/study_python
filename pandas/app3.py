from ast import Import
from http.client import ImproperConnectionState
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

df = data.DataReader('AAPL','yahoo', start="2019-01-01", end="2020-01-01")
#print(df['Close'])
df['Close'].plot()

df2 = data.DataReader('005930','naver',start ="2019-01-01", end="2020-01-01")
df2['Close'] = df2['Close'].astype(float)
#print(df2['Close'])

#print(df2['Close'].rolling(5).mean())
df2['rolling'] = df2['Close'].rolling(5).mean()
#print(df2)

plt.plot(df.index, df['Close'], color = "crimson")
plt.xlabel('time')
plt.ylabel('price')
plt.legend(['apple'])
plt.show()

plt.bar(df.index, df['Close'])
plt.show()

plt.pie([57,35,11], labels= ['ramen', 'tuna','snack'])
plt.show()

plt.hist([160,165,170,171,172,180])
plt.show()

math=[5,8,23,5,67,34,34,23]
eng=[23,6,3,1,5,45,54,34]
plt.scatter(math, eng)
plt.show()

plt.stackplot([1,2,3], [10,20,30], [30,20,50])
plt.show()

plt.figure(figsize=(10,10))
plt.plot(df.index,df['Close'])
plt.plot(df2.index,df2['Close'])
plt.show()
