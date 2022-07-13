import requests
from bs4 import BeautifulSoup

data = requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=61&query=사과&nso=&nqx_theme={"theme":{"main":{"name":"food_ingredient"}}}&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=62&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=08350105&fgn_region=&fgn_city=&lgl_lat=35.1629289&lgl_long=129.1580885&abt=&_callback=viewMoreContents')

soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
problem = soup.select('a.api_txt_lines')

print(problem[0].text)
print(problem[1].text)
print(problem[3].text)

data = requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=61&query=사과&nso=&nqx_theme={"theme":{"main":{"name":"food_ingredient"}}}&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=62&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=08350105&fgn_region=&fgn_city=&lgl_lat=35.1629289&lgl_long=129.1580885&abt=&_callback=viewMoreContents')
