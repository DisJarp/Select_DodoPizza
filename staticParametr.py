from selenium.webdriver.common.by import By

# Классы для хранения статических параметров

class StaticParametr():
    # Адреса сайта
    LINK_ONE = "https://dodopizza.ru/zheldor/nekrasova2a"
    LINK_TWO = "https://dodopizza.ru/moscow"

class PageLocators():
    # Локаторы для поисков элементов на сайте
    FIND_PIZZA = (By.CSS_SELECTOR, '#pizzas .img')
    ADD_PIZZA = (By.CSS_SELECTOR,'.icdaLa')
    CAUNT_PIZZA = (By.CSS_SELECTOR, ".hQrhEt")
    BASCET = (By.CSS_SELECTOR,".bUUipH")
    SUMMA_PIZZA_BASCET = (By.CSS_SELECTOR, "body > div:nth-child(9) > div > div.qg2lof-1.daXdIY > div > div > div:nth-child(1) > main > div > section.sc-1mxhfre-0.kNWzcY > div.subtotal > div:nth-child(1) > span")
    CAUNT_PIZZA_BASCET = (By.CSS_SELECTOR, ".EdgdS")
    POLOVINA_PIZZA = (By.CSS_SELECTOR, ".icGtaT")
    ADD_PIZZA_POLOVINA = (By.CSS_SELECTOR, ".bcGxSt")