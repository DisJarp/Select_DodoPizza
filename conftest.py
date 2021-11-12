import pytest
from selenium import webdriver
from staticParametr import StaticParametr
#Создаем параметры для выбора запуска
def pytest_addoption(parser):
    #Указание браузера который будет использоваться
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    #Указываем на какой сайт перейдем
    parser.addoption('--links', action='store', default=StaticParametr.LINK_ONE,
                     help=f"Send link: {StaticParametr.LINK_ONE} \nand\n {StaticParametr.LINK_TWO}")
    # Указываем количество пиццы
    parser.addoption('--count', action='store', default=3,
                     help="Specify the required amount of pizza")

#Фабула для выбора количества пиццы
@pytest.fixture()
def count(request):
    count = request.config.getoption("count")
    return count


#Фабула для выбора сайта
@pytest.fixture()
def link(request):
    link = request.config.getoption("links")
    if link == StaticParametr.LINK_ONE:
        print(f"Selected {StaticParametr.LINK_ONE}")
        return link
    elif link == StaticParametr.LINK_TWO:
        print(f"Selected {StaticParametr.LINK_TWO}")
        return link
    else:
        raise pytest.UsageError(f"--links should be {StaticParametr.LINK_ONE} or {StaticParametr.LINK_TWO}")


#Фабула для выбора браузера
@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()