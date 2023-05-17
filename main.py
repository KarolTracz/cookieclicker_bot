import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def start():
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    website_cookies = driver.find_element(By.CLASS_NAME, value="fc-button-label")
    website_cookies.click()
    driver.implicitly_wait(5)
    lang = driver.find_element(By.ID, value="langSelect-EN")
    lang.click()
    driver.implicitly_wait(5)
    BigCookie = driver.find_element(By.ID, value="bigCookie")
    for _ in range(120):
        BigCookie.click()
    return None


start()
time.sleep(1)


class Product:
    def __init__(self, name: str = 'NoName', price: int = 1, amount: int = 0, cps: float = 0., boost: float = 0., click=None):
        """
        :param name: Product name as a string
        :param amount: How much product is owned
        :param price:  How much product cost
        :param cps:  How many cookies per second it produces
        :param boost: How much it boost other buildings in float
        :param click: selenium WebElement object used to .click()
        """
        self.name = name
        self.amount = amount
        self.price = price
        self.cps = cps
        self.boost = boost
        self.__click = click

    def __str__(self):
        return f"""
name    {self.name}
price:  {self.price}
amount: {self.amount}
cps:    {self.cps}
boost:  {self.boost}
click_: {self.__click}
"""

    def buy(self):
        if self.price <= cookies_refresh()[0]:
            print(f'{self.name} buy for {self.price}')
            self.__click.click()

    def production(self):
        return self.amount + self.cps + self.boost


products = driver.find_elements(By.CLASS_NAME, value="content")
product_list = []
count = 0
for product in products:
    count += 1
    list_ = product.text.split('\n')
    if list_[0] != '???' and list_[0] != '':
        product_list.append(Product(list_[0], int(list_[1]), click=driver.find_element(By.ID, value=f"product{count}")))

raw_cookies_source = driver.find_element(By.ID, value="cookies")


def cookies_refresh():
    cookies_source = raw_cookies_source.text.replace(' cookies\nper second: ', ',').split(sep=',')
    cookies = int(cookies_source[0].replace(',', ''))
    cookies_per_second = float(cookies_source[1])
    return [cookies, cookies_per_second]


for i in product_list:
    i.buy()

for _ in range(10):
    time.sleep(10)
    print(cookies_refresh())

time.sleep(1)
driver.close()