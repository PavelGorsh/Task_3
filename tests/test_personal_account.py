import allure
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


'''
Проверки личного кабинета
'''

class TestPersonalAccount:

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

    @allure.title('Проверка перехода на страницу «Личный Кабинет» по клику на «Личный Кабинет» авторизированным пользователем')
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
        # Логин пользователя
        login_page.login_user(email, password)
        # Переход на страницу с разделом «Конструктор»
        const_page.wait_for_load_constructor_page()
        # Переход на страницу «Личный кабинет»
        account_page = AccountPage(driver)
        const_page.click_on_personal_account()
        account_page.wait_for_load_account_page()

        # Проверка перехода на страницу «Личный Кабинет» по клику на «Личный Кабинет» авторизированным пользователем
        account_page.check_turn_by_ckick_personal_account_btn_with_auth()

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
        # Логин пользователя
        login_page.login_user(email, password)
        # Переход на страницу с разделом «Конструктор»
        const_page.wait_for_load_constructor_page()
        # Переход на страницу «Личный кабинет»
        account_page = AccountPage(driver)
        const_page.click_on_personal_account()
        account_page.wait_for_load_account_page()

        # Переход в раздел «История заказов»
        account_page.click_on_order_history()
        account_page.wait_for_load_account_order_history_page()

        # Проверка перехода в раздел «История заказов»
        account_page.check_turn_to_order_history()

    @allure.title('Проверка выхода из аккаунта на странице «Личный Кабинет»')
    def test_exit_from_account(self, driver_user):
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
        # Логин пользователя
        login_page.login_user(email, password)
        # Переход на страницу с разделом «Конструктор»
        const_page.wait_for_load_constructor_page()
        # Переход на страницу «Личный кабинет»
        account_page = AccountPage(driver)
        const_page.click_on_personal_account()
        account_page.wait_for_load_account_page()

        # Переход на страницу «Логин» кликом на кнопку «Выход»
        account_page.click_on_exit()
        login_page.wait_for_load_login_page()

        # Проверка выхода из аккаунта
        login_page.check_turn_by_ckick_exit_btn_on_personal_account_page()
        