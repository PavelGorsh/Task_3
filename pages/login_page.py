import allure
from pages.base_page import BasePage
import locators.login_page_locators as LPL
import data
import urls


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # ОЖИДАНИЯ

    def wait_for_load_login_page(self):
        self.wait_for_load(self.driver, LPL.SIGN_IN)

    # НАЖАТИЯ

    @allure.step('Нажимаем «Войти»') 
    def click_on_sing_in(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, LPL.SIGN_IN)
        else:
            self.click_virt_mouse(self.driver, LPL.SIGN_IN)

    @allure.step('Нажимаем «Восстановить пароль»')
    def click_on_recover_password(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, LPL.RECOVER_PASSWORD)
        else:
            self.click_virt_mouse(self.driver, LPL.RECOVER_PASSWORD)

    # ВВОД ДАННЫХ В ПОЛЯ И НАЖАТИЕ

    @allure.step('Логин пользователя')    
    def login_user(self, email, password):
        self.send_keys(self.driver, LPL.SIGN_IN_EMAIL, email)
        self.send_keys(self.driver, LPL.SIGN_IN_PASSWORD, password)
        self.click_on_sing_in()

    # ПРОВЕРКИ

    @allure.step('Проверяем переход по клику на «Личный Кабинет» без авторизации')    
    def check_turn_by_ckick_personal_account_btn_without_auth(self):
        assert (urls.LOGIN_URL == self.get_current_url(self.driver) and 
                self.element_is_displayed(self.driver, LPL.SIGN_IN))
        
    @allure.step('Проверяем переход по клику на «Выход» на странице «Личный Кабинет»')    
    def check_turn_by_ckick_exit_btn_on_personal_account_page(self):
        assert (urls.LOGIN_URL == self.get_current_url(self.driver) and 
                self.element_is_displayed(self.driver, LPL.SIGN_IN))
