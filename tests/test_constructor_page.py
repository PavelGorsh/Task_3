import allure
import data
import pytest
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage



class TestConstructorPage:

    @allure.title('Проверка попадания в раздел «Конструктор»')
    def test_turn_to_constructor_page(self, driver):
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        orders_page = OrdersFeedPage(driver)
        # Перейди в раздел «Лента заказов»
        const_page.click_on_orders_feed_page_btn()
        # Добавь явное ожидание для загрузки страницы
        orders_page.wait_for_load_orders_feed_page()

        # Перейди в раздел «Конструктор»
        orders_page.click_on_constructor_page_btn()
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Проверка перехода на «Конструктор»
        const_page.check_turn_by_ckick_costructor_btn()

    @allure.title('Проверка клика на ингредиент и появления окна «Детали ингредиента»')
    def test_opening_details_window(self, driver):
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Клик на ингредиент
        const_page.click_on_ingredient_krator_bun()
        # Добавь явное ожидание для загрузки окна «Детали ингредиента»
        const_page.wait_for_load_ingredient_details_window()

        # Проверка открытия окна «Детали ингредиента»
        const_page.check_details_window()

    @allure.title('Проверка закрытия окна «Детали ингредиента» по крестику')
    def test_closing_details_window(self, driver):
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Клик на ингредиент
        const_page.click_on_ingredient_krator_bun()
        # Добавь явное ожидание для загрузки окна «Детали ингредиента»
        const_page.wait_for_load_ingredient_details_window()

        # Клик на крестик
        const_page.click_on_cross()
        # Добавь явное ожидание для закрытия окна «Детали ингредиента»
        const_page.wait_for_close_ingredient_details_window()

        # Проверка закрытия окна «Детали ингредиента»
        const_page.check_details_window_close()

    @allure.title('Проверка увеличения каунтера при добавлении ингредиента в заказ')
    @pytest.mark.parametrize('element, element_counter', data.INGREDIENT_AND_COUNTER_LIST)
    def test_drag_and_drope_ingredient(self, driver, element, element_counter):
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Перетаскивание ингредиента
        const_page.drag_and_drop_ingredient(element)

        # Проверка увеличения каунтера
        const_page.check_counter_increase(element, element_counter)        

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    def test_place_order(self, driver_user):
        driver = driver_user[0]
        email = driver_user[1][0]
        password = driver_user[1][1]
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Перетаскивание ингредиентов
        const_page.drag_and_drop_ingredient_for_test_place_order()

        # Логин пользователя
        login_page = LoginPage(driver)
        const_page.click_on_sing_in_account()
        login_page.wait_for_load_login_page()
        login_page.login_user(email, password)

        # Создание заказа
        const_page.place_order()

        # Проверка появления окна с новым созданным заказом
        const_page.check_place_order()
