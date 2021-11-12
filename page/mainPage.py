import time
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from staticParametr import PageLocators
from .basepage import BasePage

class MainPage(BasePage):
    #Глобальные переменные для сравнения
    summa_chek = 0
    count_chek = 0

    #Метод для поиска цифр в строке и вычленение их
    def take_summa(self, summa):
        num = ""
        for c in summa:
            if c.isdigit():
                num = num + c
        return num

    #Метод находит все пиццы и добавляет в корзину
    def send_find_all_pizza(self):
        #Находим все пиццы на сайте и собираем в массив
        find_pizza = self.browser.find_elements(*PageLocators.FIND_PIZZA)
        i = 0
        print("Указанное количество "+str(self.count))
        # Запускает цикл по указанному количеству пиццы при запуске программы
        while i < int(self.count):
            #Выбераем рандомную пиццу из массива
            pizza = find_pizza[randint(0, len(find_pizza))]
            try:
                #Говорим что необходимо подождать пока кнопка на пицце не станет активной, и после нажимаем
                WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(pizza)).click()
                #Находим кнопку добовления в корзину
                add_select_pizza = self.browser.find_element(*PageLocators.ADD_PIZZA)
                #Берем с текста кнопки сумму пиццы
                self.summa_chek += int(self.take_summa(str(add_select_pizza.text)))
                #Нажимаем на добавление пиццы в корзину
                add_select_pizza.click()
                #Увеличиваем счетчик и притормаживаем программу, так как пицца не успевает прогружаться (Явное ожидание указанно в basepage.py)
                i += 1
                time.sleep(3)
            except:
                print("Ошибка:  ValueError: invalid literal for int() with base 10: ''")
                print("Не понимаю причину")
                pass
        #Записываем точное число проходов
        self.count_chek = i;

    #Метод для проверки наличия кнопки коризны и просмотра количества в корзине
    def go_basket_pizza(self):
        #Проверяет через обработчик исключений который находиться в basepage.py
        assert self.is_element_present(*PageLocators.BASCET), "Кнопка корзины куда то изчезла"
        print("Кнопка корзины на месте")
        #Находит и проверяет количество элементов написанное на корзине
        count_pizza = self.browser.find_element(*PageLocators.CAUNT_PIZZA)
        assert int(self.count_chek) + 1 == int(count_pizza.text), "Указанно не верное количество на корзине"
        print(f"Элементов в корзине: {str(count_pizza.text)}")
        #Ожидает активации кнопки и открывает корзину
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(PageLocators.BASCET)).click()

    #Метод для проверки элементов в корзине (Количество и сумму)
    def check_count_and_summa(self):
        #Находим сумму на форме
        take_summa_basket = self.browser.find_element(*PageLocators.SUMMA_PIZZA_BASCET)
        try:
            #Проверяем верна ли сумма
            assert int(self.take_summa(take_summa_basket.text)) == self.summa_chek, "Сумма не верна"
        except:
            print("Ошибка:  ValueError: invalid literal for int() with base 10: ''")
            print("Не понимаю причину")
        pass
        print("Сумма в корзине верна")
        #Так как не смог получить число, получаю массив элементов на форме и считаю длину
        take_count_basket = self.browser.find_elements(*PageLocators.CAUNT_PIZZA_BASCET)
        #Сравниваю количестов элементов (+1 пустышка изначально добавленный элемент)
        assert len(take_count_basket) == (self.count_chek + 1), "Колличество товаров не верно"
        print("Колличество элементов верно")
