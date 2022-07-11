import imp #json Json Parser Online
from papago import translate #from filename import definition/import*
import pandas as pd

data = pd.read_excel('english-1.xlsx', engine='openpyxl')

for l, row in data.iterrows():    #data large itertuple()
    data.loc[l,'korean'] = translate(row['english'])

print(data)
data.to_excel('output.xlsx')

