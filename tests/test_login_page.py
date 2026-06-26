import allure
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


class TestLoginPage():

    @allure.title('Проверка перехода на страницу с разделом «Логин» по клику на «Личный кабинет»')
    def test_turn_to_login_page(self, driver):
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Переход на страницу с разделом «Логин»
        login_page = LoginPage(driver)
        const_page.click_on_personal_account()
        login_page.wait_for_load_login_page()

        # Проверка перехода на страницу с разделом «Логин» по клику на «Личный Кабинет»
        login_page.check_turn_by_ckick_personal_account_btn_without_auth()
