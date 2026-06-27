import allure
from pages.base_page import BasePage
import locators.reset_password_page_locators as RPPL
import data
import urls


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # ОЖИДАНИЯ

    def wait_for_load_reset_password_page(self):
        self.wait_for_load(self.driver, RPPL.PASSWORD_FOR_RECOVER)

    # НАЖАТИЯ

    @allure.step('Нажимаем «показать/скрыть пароль» (глаз)')  
    def click_on_eye(self):
        if(data.DRIVER_NAME == 'chrome'):
            self.click_button(self.driver, RPPL.EYE_BTN)
        else:
            self.click_virt_mouse(self.driver, RPPL.EYE_BTN)

    # ВВОД ДАННЫХ В ПОЛЯ

    @allure.step('Ввод пароля')    
    def recover_password(self, password):
        self.send_keys(self.driver, RPPL.PASSWORD_FOR_RECOVER, password)

    # ПРОВЕРКИ

    @allure.step('Проверяем переход на страницу восстановления пароля с вводом пароля')    
    def check_turn_to_reset_password_page(self):
        assert (urls.RESET_PASSWORD_URL == self.get_current_url(self.driver) and 
                self.element_is_displayed(self.driver, RPPL.RECOVERING) and
                self.element_is_displayed(self.driver, RPPL.PASSWORD_FOR_RECOVER))
        
    @allure.step('Проверяем, что поле не активно и не подсвечивается, когда глаз скрыт')    
    def check_eye_close(self):
        assert (self.element_is_displayed(self.driver, RPPL.FIELD_EYE_CLOSE) and
                self.element_is_displayed(self.driver, RPPL.LABEL_EYE_CLOSE))

    @allure.step('Проверяем, что поле активно и подсвечивается, когда глаз открыт')    
    def check_eye_open(self):
        assert (self.element_is_displayed(self.driver, RPPL.FIELD_ACTIVE_EYE_OPEN) and
                self.element_is_displayed(self.driver, RPPL.LABEL_ACTIVE_EYE_OPEN))
