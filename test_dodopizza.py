from page.mainPage import MainPage

#Тест
def test_find_and_add_pizza(browser, link, count):
    #Создаем экзепляр класса с описанием действий для теста и передаем параметры
    page = MainPage(browser, link, count)
    #Метод запуска браузера
    page.open_site()
    #Метод находит все пиццы и добавляет в корзину
    page.send_find_all_pizza()
    # Метод для проверки наличия кнопки коризны и просмотра количества в корзине
    page.go_basket_pizza()
    # Метод для проверки элементов в корзине (Количество и сумму)
    page.check_count_and_summa()

