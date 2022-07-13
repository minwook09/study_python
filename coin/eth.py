import requests
import json
import time

data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d')
#print(data.content)

line = json.loads(data.content)

for i in range(200):
    time1 = line['data'][i]['DT']
    time2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time1/1000))
    
    print(time2)
    print(line['data'][i]['Close'])

