from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

class BasePage():
    def __init__(self, browser, link, count, timeout=20):
        self.browser = browser
        self.link = link
        self.count = count
        self.browser.implicitly_wait(timeout)

    #Метод открытия сайта
    def open_site(self):
        self.browser.get(str(self.link))

    #Метод отлавливания исключения (Находится элемент на форме)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
