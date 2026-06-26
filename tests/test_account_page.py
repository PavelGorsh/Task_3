import allure
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


class TestAccountPage():

    @allure.title('Проверка перехода на страницу с разделом «Логин» по клику на «Личный кабинет»')
    def test_turn_to_account_profile_page(self, driver_user):
        driver = driver_user[0]
        email = driver_user[1][0]
        password = driver_user[1][1]
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Переход на страницу «Логин»
        login_page = LoginPage(driver)
        const_page.click_on_personal_account()
        login_page.wait_for_load_login_page()
        login_page.login_user(email, password)
        # Переход на страницу с разделом «Конструктор»
        const_page.wait_for_load_constructor_page()
        # Переход на страницу «Личный кабинет»
        profile_page = AccountPage(driver)
        const_page.click_on_personal_account()
        profile_page.wait_for_load_account_page()

        # Проверка перехода на страницу с разделом «Логин» по клику на «Личный Кабинет»
        profile_page.check_turn_by_ckick_personal_account_btn_with_auth()

    @allure.title('Проверка перехода в раздел «История заказов» на странице «Личный Кабинет»')
    def test_turn_to_order_history(self, driver_user):
        driver = driver_user[0]
        email = driver_user[1][0]
        password = driver_user[1][1]
        # через фикстуру загружается страница с разделом «Конструктор»
        const_page = ConstructorPage(driver)
        # Добавь явное ожидание для загрузки страницы
        const_page.wait_for_load_constructor_page()

        # Переход на страницу «Логин»
        login_page = LoginPage(driver)
        const_page.click_on_personal_account()
        login_page.wait_for_load_login_page()
        login_page.login_user(email, password)
        # Переход на страницу с разделом «Конструктор»
        const_page.wait_for_load_constructor_page()
        # Переход на страницу «Личный кабинет»
        profile_page = AccountPage(driver)
        const_page.click_on_personal_account()
        profile_page.wait_for_load_account_page()

        # Переход в раздел «История заказов»
        profile_page.click_on_order_history()
        profile_page.wait_for_load_account_order_history_page()

        # Проверка перехода в разделом «История заказов»
        profile_page.check_turn_to_order_history()