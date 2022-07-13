import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/sise/')

soup = BeautifulSoup(data.content,'html.parser')
print(soup.find_all( 'span',id='KOSPI_now')[0].text)

img = soup.select ('#tab_sel3_sise_main_chart > a > img')[0]
print(img)