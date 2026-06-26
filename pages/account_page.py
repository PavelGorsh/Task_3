import allure
from pages.base_page import BasePage
import locators.account_page_locators as APL
import urls


class AccountPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # ОЖИДАНИЯ

    def wait_for_load_account_page(self):
        self.wait_for_load(self.driver, APL.PROFILE_BTN)

    def wait_for_load_account_order_history_page(self):
        self.wait_for_load(self.driver, APL.HISTORY_BTN_ACTIVE)

    # НАЖАТИЯ

    @allure.step('Нажимаем «История заказов»')
    def click_on_order_history(self):
        self.click_button(self.driver, APL.HISTORY_BTN)

    # ВВОД ДАННЫХ В ПОЛЯ И НАЖАТИЕ



    # ПРОВЕРКИ

    @allure.step('Проверяем переход по клику на «Личный Кабинет» с авторизацией')    
    def check_turn_by_ckick_personal_account_btn_with_auth(self):
        assert (urls.ACCOUNT_PROFILE_URL == self.get_current_url(self.driver) and 
                self.element_is_displayed(self.driver, APL.PROFILE_BTN_ACTIVE))
        
    @allure.step('Проверяем переход в раздел «История заказов»')    
    def check_turn_to_order_history(self):
        assert (urls.ACCOUNT_ORDER_HISTORY_URL == self.get_current_url(self.driver) and 
                self.element_is_displayed(self.driver, APL.HISTORY_BTN_ACTIVE))