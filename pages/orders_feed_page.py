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

    def wait_for_load_orders(self):
        self.wait_for_load(self.driver, OFPL.UPPER_ORDER_TITLE)

    def wait_for_load_quantity(self):
        self.wait_for_load(self.driver, OFPL.ORDERS_QUANTITY_ALL_TIME)
        self.wait_for_load(self.driver, OFPL.ORDERS_QUANTITY_TODAY)

    def wait_for_change_orders_in_work_to_number(self):
        self.wait_for_change_text_of_element(self.driver, OFPL.ID_ORDER_LIST_FROM_IN_WORK, "Все текущие заказы готовы!")

    # НАЖАТИЯ

    @allure.step('Нажимаем «Конструктор» в разделе «Лента заказов»')
    def click_on_constructor_page_btn(self):
        self.click_button(self.driver, OFPL.CONSTRUCT_BURGER_HEADER_BTN)

    @allure.step('Нажимаем на верхний заказ')
    def click_on_upper_order(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, OFPL.UPPER_ORDER)
        else:
            self.click_virt_mouse(self.driver, OFPL.UPPER_ORDER)

    # ПОЛУЧЕНИЕ ДАННЫХ

    @allure.step('Получаем список заказов из раздела «Лента заказов»')
    def get_ids_orders(self):
        elements_list = self.get_id_order_elements_list(self.driver, OFPL.ID_ORDER_LIST_FROM_ORDERS_FEED)
        elements_list_text = []
        for item in elements_list:
            elements_list_text.append(item.text)
        return elements_list_text
    
    @allure.step('Получаем список заказов из раздела «Готовы»')
    def get_ids_orders_complited(self):
        elements_list = self.get_id_order_elements_list(self.driver, OFPL.ID_ORDER_LIST_FROM_COMPLITED)
        elements_list_text = []
        for item in elements_list:
            elements_list_text.append(item.text)
        return elements_list_text
    
    @allure.step('Получаем список заказов из раздела «В работе»')
    def get_ids_orders_in_work(self):
        elements_list = self.get_id_order_elements_list(self.driver, OFPL.ID_ORDER_LIST_FROM_IN_WORK)
        elements_list_text = []
        for item in elements_list:
            elements_list_text.append(item.text)
        return elements_list_text
    
    @allure.step('Получаем название верхнего заказа')
    def get_title_upper_order(self):
        self.wait_for_load_orders()
        return self.get_text_attribute(self.driver, OFPL.UPPER_ORDER_TITLE)
    
    @allure.step('Получаем количество созданных заказов за все время')
    def get_orders_quantity_all_time(self):
        return self.get_text_attribute(self.driver, OFPL.ORDERS_QUANTITY_ALL_TIME)
    
    @allure.step('Получаем количество созданных заказов за сегодня')
    def get_orders_quantity_today(self):
        return self.get_text_attribute(self.driver, OFPL.ORDERS_QUANTITY_TODAY)
    
    def get_orders_quantity(self, period):
        self.wait_for_load_quantity()
        quantity = 0
        if period == "all_time":
            quantity = self.get_orders_quantity_all_time()
        else:
            quantity = self.get_orders_quantity_today()
        return quantity

    # ПРОВЕРКИ

    @allure.step('Проверяем переход по клику на «Лента заказов»')
    def check_turn_by_ckick_orders_feed_btn(self):
        assert urls.ORDERS_FEED_URL == self.get_current_url(self.driver) and self.element_is_displayed(self.driver, OFPL.ORDERS_FEED_HEADER_BTN_ACTIVE)

    @allure.step('Проверяем появление окна «Детали заказа»')
    def check_details_window(self, order_title):
        assert (order_title == self.get_text_attribute(self.driver, OFPL.DETAILS_WINDOW_TITLE) and 
                "Cостав" == self.get_text_attribute(self.driver, OFPL.DETAILS_WINDOW_CONTAIN) and # В коде программы буква С написана латиницей
                self.element_is_displayed(self.driver, OFPL.DETAILS_WINDOW_TITLE))

    @allure.step('Проверяем нахождение созданного заказа в разделе «История заказов» и на странице «Лента заказов»') 
    def check_contain_placed_order_from_history_in_orders_feed(self, id_order_from_order_window, id_order_from_order_history):
        id_order_from_order_window_mod = "#0" + id_order_from_order_window
        self.wait_for_load_orders()
        ids_orders_list = self.get_ids_orders()
        assert (id_order_from_order_window_mod in ids_orders_list and 
                id_order_from_order_history in ids_orders_list and 
                id_order_from_order_window_mod == id_order_from_order_history)
        
    @allure.step('Проверяем нахождения созданного заказа на странице «Лента заказов» в разделе «Готовы», в разделе «В работе» (по отдельности)')
    def check_contain_placed_order_in_complited_and_in_work(self, id_order_from_order_window, status):
        id_order_from_order_window_mod = "0" + id_order_from_order_window
        self.wait_for_load_orders()
        if status == "complited":
            ids_orders_list = self.get_ids_orders_complited()
        else:
            self.wait_for_change_orders_in_work_to_number()
            ids_orders_list = self.get_ids_orders_in_work()
        assert (id_order_from_order_window_mod in ids_orders_list)
    
    @allure.step('Проверяем увеличение счётчиков заказов при создании нового заказа')
    def check_increase_orders_quantity_in_orders_feed(self, before_new_order, after_new_order):
        assert (before_new_order < after_new_order)
