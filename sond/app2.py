from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://instagram.com')


time.sleep(2)
p = driver.find_element_by_css_selector('.KPnG0')
p.click()

time.sleep(2)
e = driver.find_element_by_css_selector('input[name="email"]')
e.send_keys('01038307943')
r = driver.find_element_by_css_selector('input[name="pass"]')
r.send_keys('qok513476@@')
r.send_keys(Keys.ENTER)
time.sleep(4)
t = driver.find_element_by_css_selector('._a9_1')
t.click()

#페이지 이동
driver.get('https://www.instagram.com/explore/tags/%EC%BD%94%EB%94%A9/')
#첫번째사진
driver.implicitly_wait(10)
first = driver.find_element_by_css_selector('._aagv').click()



#time.sleep(2)
#e = driver.find_element_by_css_selector('input[name="username"]').text
#print(e)
