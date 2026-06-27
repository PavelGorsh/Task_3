import allure
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:

    @allure.title('Проверка неактивного поля «Пароль» (глаз закрыт) при открытии страницы')
    def test_eye_close(self, driver_user):
        driver = driver_user[0]
        email = driver_user[1][0]
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Переход на страницу с разделом «Логин»
        login_page = LoginPage(driver)
        const_page.click_on_personal_account()
        login_page.wait_for_load_login_page()

        # Переход на страницу с разделом «Восстановление пароля - ввод email»
        forgot_page = ForgotPasswordPage(driver)
        login_page.click_on_recover_password()
        forgot_page.wait_for_load_forgot_password_page()

        # Переход на страницу с разделом «Восстановление пароля - ввод пароля»
        reset_page = ResetPasswordPage(driver)
        # Восстановление пароля (ввод почты и клик по кнопке «Восстановить»)
        forgot_page.click_on_recover_with_input_email(email)
        reset_page.wait_for_load_reset_password_page()

        # Проверка скрытого пароля
        reset_page.check_eye_close()

    @allure.title('Проверка клика по кнопке «показать/скрыть пароль», чтобы подсветить поле «Пароль» и сделать его активным')
    def test_eye_open(self, driver_user):
        driver = driver_user[0]
        email = driver_user[1][0]
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Переход на страницу с разделом «Логин»
        login_page = LoginPage(driver)
        const_page.click_on_personal_account()
        login_page.wait_for_load_login_page()

        # Переход на страницу с разделом «Восстановление пароля - ввод email»
        forgot_page = ForgotPasswordPage(driver)
        login_page.click_on_recover_password()
        forgot_page.wait_for_load_forgot_password_page()

        # Переход на страницу с разделом «Восстановление пароля - ввод пароля»
        reset_page = ResetPasswordPage(driver)
        # Восстановление пароля (ввод почты и клик по кнопке «Восстановить»)
        forgot_page.click_on_recover_with_input_email(email)
        reset_page.wait_for_load_reset_password_page()

        # Нажатие на глаз (изначально глаз закрыт)
        reset_page.click_on_eye()

        # Проверка скрытого пароля
        reset_page.check_eye_open()

    @allure.title('Проверка клика по кнопке «показать/скрыть пароль» два раза, чтобы сделать активным поле «Пароль», а потом сделать его снова неактивным')
    def test_eye_close_after_opening(self, driver_user):
        driver = driver_user[0]
        email = driver_user[1][0]
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Переход на страницу с разделом «Логин»
        login_page = LoginPage(driver)
        const_page.click_on_personal_account()
        login_page.wait_for_load_login_page()

        # Переход на страницу с разделом «Восстановление пароля - ввод email»
        forgot_page = ForgotPasswordPage(driver)
        login_page.click_on_recover_password()
        forgot_page.wait_for_load_forgot_password_page()

        # Переход на страницу с разделом «Восстановление пароля - ввод пароля»
        reset_page = ResetPasswordPage(driver)
        # Восстановление пароля (ввод почты и клик по кнопке «Восстановить»)
        forgot_page.click_on_recover_with_input_email(email)
        reset_page.wait_for_load_reset_password_page()

        # Нажатие на глаз (изначально глаз закрыт)
        reset_page.click_on_eye()

        # Нажатие на глаз (чтобы сделать его снова закрытым, после того как он был открыт по предыдущему клику)
        reset_page.click_on_eye()

        # Проверка скрытого пароля
        reset_page.check_eye_close()
        