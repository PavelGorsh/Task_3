import allure
from pages.base_page import BasePage
import locators.forgot_password_page_locators as FPPL
import data
import urls


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # ОЖИДАНИЯ

    def wait_for_load_forgot_password_page(self):
        self.wait_for_load(self.driver, FPPL.EMAIL_FOR_RECOVER)

    # НАЖАТИЯ

    @allure.step('Нажимаем «Восстановить»')
    def click_on_recover(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, FPPL.RECOVER_BTN)
        else:
            self.click_virt_mouse(self.driver, FPPL.RECOVER_BTN)

    # ВВОД ДАННЫХ В ПОЛЯ И НАЖАТИЕ

    @allure.step('Вводим email')    
    def click_on_recover_with_input_email(self, email):
        self.send_keys(self.driver, FPPL.EMAIL_FOR_RECOVER, email)
        self.click_on_recover()

    # ПРОВЕРКИ

    @allure.step('Проверяем переход на страницу восстановления пароля с вводом email')    
    def check_turn_to_forgot_password_page(self):
        assert (urls.FORGOT_PASSWORD_URL == self.get_current_url(self.driver) and 
                self.element_is_displayed(self.driver, FPPL.RECOVERING) and
                self.element_is_displayed(self.driver, FPPL.EMAIL_FOR_RECOVER))
