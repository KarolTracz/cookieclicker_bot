# import time
# import re
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome(executable_path="C:\\Users\\lolek\\chromedriver\\chromedriver.exe")
# driver.get('https://orteil.dashnet.org/cookieclicker/')
# driver.maximize_window()
# cookies = driver.find_element(By.CLASS_NAME, value="fc-button-label")
# cookies.click()
# driver.implicitly_wait(60)
# lang = driver.find_element(By.ID, value="langSelect-EN")
# lang.click()
# driver.implicitly_wait(60)
# time.sleep(2)
# BigCookie = driver.find_element(By.ID, value="bigCookie")
# driver.implicitly_wait(60)
# for _ in range(15):
#     BigCookie.click()
# cursor = driver.find_element(By.ID, value="product0")
# cursor.click()
# """
# <div id="cookies" class="title">124.611<br>million cookies<div id="cookiesPerSecond">per second: 237,284</div></div>
# """
# # farm = driver.find_element(By.ID, value="product2")
# # farm.click()
# driver.implicitly_wait(1)
# cookies_source = driver.find_element(By.ID, value="cookies")
# pattern = r'<div id="cookies" class="title">([\d\.,]+)<br>([\w\s]+) cookies<div id="cookiesPerSecond">per second: ([\d\.,]+)<\/div><\/div>'
# match = re.search(pattern, cookies_source.text)
#
# if match:
#     cookies = int(float(match.group(1).replace(',', '')))
#     attribute = match.group(2)
#     cookies_per_second = int(match.group(3).replace(',', ''))
#
#     print("Cookies:", cookies)
#     print("Attribute:", attribute)
#     print("Cookies per second:", cookies_per_second)
#
#
# driver.implicitly_wait(1)
# cursor_cost = driver.find_element(By.ID, value="productPrice0")
#
# for _ in range(100):
#     time.sleep(1)
#     print('cookies: ', cookies)
#     print('cookies.text[:-24]: ', cookies_source.text)
#     print('cursor_cost.text: ', cursor_cost.text)
#     for _ in range(30):
#         BigCookie.click()
#     if int(cursor_cost.text) <= int(cookies.text):
#         print(f'cursor buy for {cursor_cost.text}')
#         cursor.click()
#
# # for i in range(20):
# #     products_names = driver.find_elements(By.ID, value=f"productName{i}")
# #     print(products_names.text)
# time.sleep(10)
# driver.close()
# """
# <div id="cookies" class="title">334 cookies<div id="cookiesPerSecond">per second: 1</div></div>
# """

import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By

cookies_value = None
attribute = None
cookies_per_second = None

driver = webdriver.Chrome(executable_path="C:\\Users\\lolek\\chromedriver\\chromedriver.exe")
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.maximize_window()
cookies = driver.find_element(By.CLASS_NAME, value="fc-button-label")
cookies.click()
driver.implicitly_wait(60)
lang = driver.find_element(By.ID, value="langSelect-EN")
lang.click()
driver.implicitly_wait(60)
time.sleep(2)
BigCookie = driver.find_element(By.ID, value="bigCookie")
driver.implicitly_wait(60)
for _ in range(15):
    BigCookie.click()
cursor = driver.find_element(By.ID, value="product0")
cursor.click()

cookies_source = driver.find_element(By.CLASS_NAME, value="title")
pattern = r'<div id="cookies" class="title">([\d\.,]+)\s*(million|billion|trillion)?\s*cookies.*?<div id="cookiesPerSecond">per second: ([\d\.,]+)<\/div>'
match = re.search(pattern, cookies_source.text)

if match:
    cookies_value = int(float(match.group(1).replace(',', '')))
    attribute = match.group(2)
    cookies_per_second = int(match.group(3).replace(',', ''))

    print("Cookies:", cookies_value)
    print("Attribute:", attribute)
    print("Cookies per second:", cookies_per_second)

cursor_cost = driver.find_element(By.ID, value="productPrice0")

for _ in range(10):
    time.sleep(1)
    if cookies_value is not None:
        print('cookies_value:', cookies_value)
    print('cursor_cost.text:', cursor_cost.text)
    for _ in range(30):
        BigCookie.click()
    if cookies_value is not None and int(cursor_cost.text) <= cookies_value:
        print(f'cursor buy for {cursor_cost.text}')
        cursor.click()

time.sleep(10)
driver.close()

