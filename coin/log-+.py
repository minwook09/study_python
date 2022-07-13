import requests
import json
import time

url = [
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time=1587600000000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time=1587600000000',
    https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time=1570406400000,
    https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time=1570406400000,
    https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time=1553212800000,
    https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time=1553212800000,
    https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time=1536019200000,
    https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time=1536019200000,
    https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time=1518825600000
]

def hkatn(a):
    data = requests.get(a)
    dicton = json.load(data.content)
    return dicton['data'][0]['Close']
    
hkatn(url[0])