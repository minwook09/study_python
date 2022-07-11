from re import T
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
from selenium.webdriver.chrome.options import Options

옵션 = webdriver.ChromeOptions()
옵션.add_argument(r'user-data-dir=C:\Users\AMD\AppData\Local\Google\Chrome\User Data\Profile2')

driver = webdriver.Chrome('chromedriver.exe', chrome_options=옵션)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144')

time.sleep(2)

pyperclip.copy('minwook09')
e = driver.find_element_by_css_selector('#id')
e.send_keys(Keys.CONTROL, 'v')

time.sleep(2)

pyperclip.copy('Athena1616@@')
e = driver.find_element_by_css_selector('#pw')
e.send_keys(Keys.CONTROL, 'v')

time.sleep(1)
e.send_keys(Keys.ENTER)


time.sleep(2)
driver.get('https://m.blog.naver.com/FeedList.naver')
time.sleep(1.5)
driver.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FFeedList.naver')

time.sleep(2)
lkn = driver.find_element_by_css_selector('#se_component_wrapper > div:nth-child(1) > div > div.se_sectionArea.se_align-left > div > div > div > div > textarea')
lkn.send_keys('블로그 제목')


lkn = driver.find_element_by_css_selector('#se_component_wrapper > div:nth-child(2) > div > div > div > div.se_viewArea.se_ff_nanumgothic.se_align-left.se_fs_T3 > div > div > div > div')
lkn.send_keys('블로그 내용입니다. \n 오늘 좆같은 일이 너무 많아요')
lkn.send_keys(Keys.ENTER)
lkn.send_keys('ㅋㅋㅋ 개같은 인생')
