import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\lolek\\chromedriver\\chromedriver.exe")


def start():
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    website_cookies = driver.find_element(By.CLASS_NAME, value="fc-button-label")
    website_cookies.click()
    driver.implicitly_wait(5)
    lang = driver.find_element(By.ID, value="langSelect-EN")
    lang.click()
    driver.implicitly_wait(5)
    time.sleep(2)
    BigCookie = driver.find_element(By.ID, value="bigCookie")
    driver.implicitly_wait(5)
    for _ in range(16):
        BigCookie.click()
    cursor = driver.find_element(By.ID, value="product0")
    cursor.click()
    return None


start()

count = 0

try:
    xyz = driver.find_elements(By.CLASS_NAME, value="content")
    for details in xyz:
        count += 1
        print('count:', count, details.text.split('\n'))
except TypeError:
    print('TypeError')

time.sleep(10)
driver.close()

