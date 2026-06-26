import allure
from pages.base_page import BasePage
import locators.constructor_page_locators as CPL
import data
import urls


class ConstructorPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # ОЖИДАНИЯ

    def wait_for_load_constructor_page(self):
        self.wait_for_load(self.driver, CPL.CONSTRUCT_BURGER_HEADER_BTN_ACTIVE)

    def wait_for_load_ingredient_details_window(self):
        self.wait_for_load(self.driver, CPL.DETAILS_WINDOW)

    def wait_for_close_ingredient_details_window(self):
        self.wait_element_until_invisibility(self.driver, CPL.DETAILS_WINDOW)

    def wait_for_load_id_order_window(self):
        self.wait_for_load(self.driver, CPL.ID_ORDER_WINDOW)
    
    def wait_for_change_id_in_order_window(self):
        self.wait_for_change_text_of_element(self.driver, CPL.ID_CREATED_ORDER, "9999")

    # НАЖАТИЯ

    @allure.step('Нажимаем на кнопку «Лента заказов» в разделе «Конструктор»')
    def click_on_orders_feed_page_btn(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, CPL.ORDERS_FEED_HEADER_BTN)
        else:
            self.click_virt_mouse(self.driver, CPL.ORDERS_FEED_HEADER_BTN)

    @allure.step('Нажимаем на один из ингредиентов - Краторная булка N-200i')
    def click_on_ingredient_krator_bun(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, CPL.INGR_KRATOR_BUN)
        else:
            self.click_virt_mouse(self.driver, CPL.INGR_KRATOR_BUN)

    @allure.step('Нажимаем крестик')
    def click_on_cross(self):
        self.click_button(self.driver, CPL.CROSS_BTN)

    @allure.step('Нажимаем «Войти в аккаунт»')
    def click_on_sing_in_account(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, CPL.SIGN_IN_ACCOUNT)
        else:
            self.click_virt_mouse(self.driver, CPL.SIGN_IN_ACCOUNT)

    @allure.step('Нажимаем «Оформить заказ»')
    def place_order(self):
        self.click_button(self.driver, CPL.PLACE_ORDER_BTN)

    @allure.step('Нажимаем «Личный кабинет»')
    def click_on_personal_account(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, CPL.PERSONAL_ACCOUNT)
        else:
            self.click_virt_mouse(self.driver, CPL.PERSONAL_ACCOUNT)

    # ПЕРЕТАСКИВАНИЯ

    @allure.step('Перетаскиваем ингредиент в корзину')
    def drag_and_drop_ingredient(self, element):
        if(data.DRIVER_NAME == 'chrome'):
            self.my_drag_and_drop(self.driver, element, CPL.BASKET_ZONE)
        else:
            self.drag_and_drop_firefox(self.driver, element, CPL.BASKET_ZONE)

    def drag_and_drop_ingredient_for_test_place_order(self):
        self.drag_and_drop_ingredient(CPL.INGR_FLUOR_BUN)
        self.drag_and_drop_ingredient(CPL.INGR_SPICY_SAUCE)
    
    # ПРОВЕРКИ

    @allure.step('Проверяем переход по клику на «Конструктор»')
    def check_turn_by_ckick_costructor_btn(self):
        assert urls.CONSTRUCTOR_URL == self.get_current_url(self.driver) and self.element_is_displayed(self.driver, CPL.CONSTRUCT_BURGER_HEADER_BTN_ACTIVE)

    @allure.step('Проверяем появление окна «Детали ингредиента»')
    def check_details_window(self):
        assert ("Детали ингредиента" == self.get_text_attribute(self.driver, CPL.DETAILS_WINDOW_TITLE) and 
                "Краторная булка N-200i" == self.get_text_attribute(self.driver, CPL.DETAILS_WINDOW_KRATOR_BUN) and
                self.element_is_displayed(self.driver, CPL.DETAILS_WINDOW))
        
    @allure.step('Проверяем закрытие окна «Детали ингредиента»')
    def check_details_window_close(self):
        assert self.element_is_not_displayed(self.driver, CPL.DETAILS_WINDOW_CLOSED)

    @allure.step('Проверяем увеличение каунтера при добавлении ингредиента в корзину')
    def check_counter_increase(self, element, element_counter):
        counter = 0
        if element == CPL.INGR_KRATOR_BUN or element == CPL.INGR_FLUOR_BUN:
            counter += 2
        else:
            counter += 1
        assert str(counter) == self.get_text_attribute(self.driver, element_counter)

    @allure.step('Проверяем появление окна с новым созданным заказом')
    def check_place_order(self):
        self.wait_for_load_id_order_window()
        self.wait_for_change_id_in_order_window()
        assert (self.element_is_displayed(self.driver, CPL.ID_ORDER_WINDOW) and 
                self.element_is_displayed(self.driver, CPL.ID_CREATED_ORDER) and 
                self.get_text_attribute(self.driver, CPL.ID_ORDER_WINDOW) != "9999")
