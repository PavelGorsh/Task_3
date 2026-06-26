import allure
from pages.constructor_page import ConstructorPage
from pages.orders_feed_page import OrdersFeedPage


class TestOrdersFeedPage:
    @allure.title('Проверка попадания в раздел «Лента заказов»')
    def test_turn_to_orders_feed_page(self, driver):
        # через фикстуру загружается страница с разделом «Конструктор»
        orders_page = OrdersFeedPage(driver)
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Перейди в раздел «Лента заказов»
        const_page.click_on_orders_feed_page_btn()
        # Добавь явное ожидание для загрузки страницы
        orders_page.wait_for_load_orders_feed_page()
        
        # Проверка перехода на «Лента заказов»
        orders_page.check_turn_by_ckick_orders_feed_btn()

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

        # Клик на заказ
        order_title = orders_page.click_on_upper_order()
        # Добавь явное ожидание для загрузки окна «Детали заказа»
        orders_page.wait_for_load_order_details_window()

        # Проверка открытия окна «Детали ингредиента»
        orders_page.check_details_window(order_title)
