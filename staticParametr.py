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
    SUMMA_PIZZA_BASCET = (By.CSS_SELECTOR, ".info:nth-child(1) > span")
    CAUNT_PIZZA_BASCET = (By.CSS_SELECTOR, ".eqA-DGO")