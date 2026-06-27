import allure
import pytest
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage


'''
Проверки раздела «Лента заказов»
'''

class TestOrdersFeed:

    @allure.title('Проверка клика на заказ и появления окна «Детали заказа»')
    def test_opening_details_window(self, driver):
        # через фикстуру загружается страница с разделом «Конструктор»
        orders_page = OrdersFeedPage(driver)
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Перейди в раздел «Лента заказов»
        const_page.click_on_orders_feed_page_btn()
        # Добавь явное ожидание для загрузки страницы
        orders_page.wait_for_load_orders_feed_page()

        # Получение названия верхнего заказа
        order_title = orders_page.get_title_upper_order()

        # Клик на заказ
        orders_page.click_on_upper_order()
        # Добавь явное ожидание для загрузки окна «Детали заказа»
        orders_page.wait_for_load_order_details_window()

        # Проверка открытия окна «Детали ингредиента»
        orders_page.check_details_window(order_title)

    @allure.title('Проверка нахождения заказа пользователя в разделе «История заказов» и на странице «Лента заказов»')
    def test_contain_placed_order_from_history_in_orders_feed(self, driver_user):
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
        const_page.click_place_order()

        # Получение номера заказа из окна созданного заказа
        const_page.wait_for_load_id_order_window()
        const_page.wait_for_change_id_in_order_window()
        id_order_from_order_window = const_page.get_id_order()

        # Закрытие окна с заказом
        const_page.click_on_cross()
        const_page.wait_for_close_id_order_window()

        # Переход на страницу «Личный кабинет»
        account_page = AccountPage(driver)
        const_page.click_on_personal_account()
        account_page.wait_for_load_account_page()

        # Переход в раздел «История заказов»
        account_page.click_on_order_history()
        account_page.wait_for_load_account_order_history_page()

        # Получение номера заказа из раздела «История заказов»
        id_order_from_order_history = account_page.get_id_order()

        # Переход на страницу «Лента заказов»
        orders_page = OrdersFeedPage(driver)
        const_page.click_on_orders_feed_page_btn()
        orders_page.wait_for_load_orders_feed_page()

        # Проверка нахождения созданного заказа на странице «Лента заказов»
        orders_page.check_contain_placed_order_from_history_in_orders_feed(id_order_from_order_window, id_order_from_order_history)

    @allure.title('Проверка нахождения заказа на странице «Лента заказов» в разделе «Готовы» и в разделе «В работе» после создания заказа')
    @pytest.mark.parametrize('status', ["complited", "in_work"])
    def test_contain_placed_order_in_complited_and_in_work(self, driver_user, status):
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
        const_page.click_place_order()

        # Получение номера заказа из окна созданного заказа
        const_page.wait_for_load_id_order_window()
        const_page.wait_for_change_id_in_order_window()
        id_order_from_order_window = const_page.get_id_order()

        # Закрытие окна с заказом
        const_page.click_on_cross()
        const_page.wait_for_close_id_order_window()

        # Переход на страницу «Лента заказов»
        orders_page = OrdersFeedPage(driver)
        const_page.click_on_orders_feed_page_btn()
        orders_page.wait_for_load_orders_feed_page()

        # Проверка нахождения созданного заказа на странице «Лента заказов» в разделе «Готовы», в разделе «В работе»
        orders_page.check_contain_placed_order_in_complited_and_in_work(id_order_from_order_window, status)

    @allure.title('Проверка увеличение счётчиков «Выполнено за всё время» и «Выполнено за сегодня» при создании нового заказа')
    @pytest.mark.parametrize('period', ["all_time", "today"])
    def test_increase_orders_quantity_in_orders_feed(self, driver_user, period):
        driver = driver_user[0]
        email = driver_user[1][0]
        password = driver_user[1][1]
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Переход на страницу «Лента заказов»
        orders_page = OrdersFeedPage(driver)
        const_page.click_on_orders_feed_page_btn()
        orders_page.wait_for_load_orders_feed_page()

        # Получение количества созданных заказов
        orders_quantity_before_new_order = orders_page.get_orders_quantity(period)

        # Перейди в раздел «Конструктор»
        orders_page.click_on_constructor_page_btn()
        const_page.wait_for_load_constructor_page()

        # Перетаскивание ингредиентов
        const_page.drag_and_drop_ingredient_for_test_place_order()

        # Логин пользователя
        login_page = LoginPage(driver)
        const_page.click_on_sing_in_account()
        login_page.wait_for_load_login_page()
        login_page.login_user(email, password)

        # Создание заказа
        const_page.click_place_order()

        const_page.wait_for_load_id_order_window()
        const_page.wait_for_change_id_in_order_window()

        # Закрытие окна с заказом
        const_page.click_on_cross()
        const_page.wait_for_close_id_order_window()

        # Переход на страницу «Лента заказов»
        const_page.click_on_orders_feed_page_btn()
        orders_page.wait_for_load_orders_feed_page()

        # Получение количества созданных заказов
        orders_quantity_after_new_order = orders_page.get_orders_quantity(period)

        # Проверка увеличения счётчиков заказов
        orders_page.check_increase_orders_quantity_in_orders_feed(orders_quantity_before_new_order, orders_quantity_after_new_order)
