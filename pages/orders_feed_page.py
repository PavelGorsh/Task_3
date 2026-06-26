import allure
from pages.base_page import BasePage
import locators.orders_feed_page_locators as OFPL
import data
import urls


class OrdersFeedPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # ОЖИДАНИЯ
    
    def wait_for_load_orders_feed_page(self):
        self.wait_for_load(self.driver, OFPL.ORDERS_FEED_HEADER_BTN_ACTIVE)

    def wait_for_load_order_details_window(self):
        self.wait_for_load(self.driver, OFPL.DETAILS_WINDOW_CONTAIN)

    # НАЖАТИЯ

    @allure.step('Нажимаем на кнопку «Конструктор» в разделе «Лента заказов»')
    def click_on_constructor_page_btn(self):
        self.click_button(self.driver, OFPL.CONSTRUCT_BURGER_HEADER_BTN)

    @allure.step('Нажимаем на верхний заказ')
    def click_on_upper_order(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, OFPL.UPPER_ORDER)
        else:
            self.click_virt_mouse(self.driver, OFPL.UPPER_ORDER)
        return self.get_text_attribute(self.driver, OFPL.UPPER_ORDER_TITLE)

    # ПЕРЕТАСКИВАНИЯ



    # ПРОВЕРКИ

    @allure.step('Проверяем переход по клику на «Лента заказов»')
    def check_turn_by_ckick_orders_feed_btn(self):
        assert urls.ORDERS_FEED_URL == self.get_current_url(self.driver) and self.element_is_displayed(self.driver, OFPL.ORDERS_FEED_HEADER_BTN_ACTIVE)

    @allure.step('Проверяем появление окна «Детали заказа»')
    def check_details_window(self, order_title):
        assert (order_title == self.get_text_attribute(self.driver, OFPL.DETAILS_WINDOW_TITLE) and 
                "Cостав" == self.get_text_attribute(self.driver, OFPL.DETAILS_WINDOW_CONTAIN) and # В коде программы буква С написана латиницей
                self.element_is_displayed(self.driver, OFPL.DETAILS_WINDOW_TITLE))


        