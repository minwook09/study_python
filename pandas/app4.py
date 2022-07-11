import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

#df = data.DataReader('AMZN','yahoo', start="2020-01-01", end="2020-12-31")
#df['Close'] = df['Close'].astype(float)
#df['rolling20'] = df['Close'].rolling(20).mean()
#df['rolling60'] = df['Close'].rolling(60).mean()

#plt.figure(figsize=(10,10))
#plt.plot(df.index,df['rolling20'])
#plt.plot(df.index,df['rolling60'])
#plt.legend(['rolling20','rolling60'])
#plt.xlabel('time')
#plt.ylabel('price')
#plt.show()

#df2 = pd.DataFrame({'':[2018,2019,2020,2021],'Samsung':[50000,60000,75000,70000],'LG':[30000,40000,50000,35000]})
#print(df2)

#plt.plot(df2[''],df2['Samsung'])
#plt.plot(df2[''],df2['LG'])
#plt.legend(['Samsung','LG'])
#plt.xlabel('time')
#plt.ylabel('price')
#plt.show()


df3 = data.DataReader('BTC-USD','yahoo', start="2020-01-01", end="2020-12-31")
meean = df3['Volume'].mean()

df3['tf'] = df3['Volume'] > meean
a= df3[df3['tf']==True]

plt.bar(a.index, a['Close'])
plt.show()