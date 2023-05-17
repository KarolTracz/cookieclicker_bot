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
    return None


start()
time.sleep(1)
BigCookie = driver.find_element(By.ID, value="bigCookie")


def first_buy():
    for _ in range(110):
        BigCookie.click()
    local_cursor = driver.find_element(By.ID, value="product0")
    local_cursor.click()


first_buy()


class Product:
    def __init__(self, name: str = 'NoName', amount: int = 0, price: int = 1, cps: float = 0, boost: float = 0, click=None):
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
name    {type(self.name)}{self.name}
amount: {type(self.amount)}{self.amount}
price:  {type(self.price)}{self.price}
cps:    {type(self.cps)}{self.cps}
boost:  {type(self.boost)}{self.boost}
click_: {type(self.__click)}{self.__click}
"""

    def buy(self):
        if self.price <= cookies_refresh()[0]:
            print(f'{self.name} buy for {self.price}')
            self.__click.click()

    def production(self):
        return self.amount + self.cps + self.boost


products = driver.find_elements(By.CLASS_NAME, value="content")
product_list = []
product_dict = {}
iteration = 0
for product in products:
    iteration += 1
    list_ = product.text.split('\n')
    if list_[0] != '???' and list_[0] != '':
        product_list.append(Product(list_[0]))
    product_dict.update({f'product{iteration}': list_})


cursor = Product(
    driver.find_element(By.ID, value="productName0").text,
    int(driver.find_element(By.ID, value="productOwned0").text),
    int(driver.find_element(By.ID, value="productPrice0").text),
    click=driver.find_element(By.ID, value="product0"),
    # driver.find_element(By.ID, value="productName0"),
    # driver.find_element(By.ID, value="productName0"),
)


# def product_refresh():
#     pass


def cookies_refresh():
    raw_cookies_source = driver.find_element(By.ID, value="cookies")
    driver.implicitly_wait(5)
    cookies_source = raw_cookies_source.text.replace(' cookies\nper second: ', ',').split(sep=',')
    cookies = int(cookies_source[0].replace(',', ''))
    cookies_per_second = float(cookies_source[1])
    return [cookies, cookies_per_second]


for i in product_list:
    print(i)
print(product_dict)

time.sleep(1)
driver.close()
