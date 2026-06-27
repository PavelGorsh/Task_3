import pytest
from selenium import webdriver
from methods.user_methods import UserMethods
import data
import urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
        data.DRIVER_NAME = 'chrome'
    else:
        browser = webdriver.Firefox()
        data.DRIVER_NAME = 'firefox'

    # переход на страницу Stellar Burgers
    browser.get(urls.CONSTRUCTOR_URL)
    yield browser

    browser.quit()

@pytest.fixture(params=["chrome", "firefox"])
def driver_user(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
        data.DRIVER_NAME = 'chrome'
    else:
        browser = webdriver.Firefox()
        data.DRIVER_NAME = 'firefox'

    # переход на страницу Stellar Burgers
    browser.get(urls.CONSTRUCTOR_URL)

    # Создание пользователя
    user_methods = UserMethods()
    user_data = user_methods.generate_new_user_data()
    response_user_data, _ = user_methods.create_user(user_data[0], user_data[1], user_data[2]) # email, password, name
    token = response_user_data.get('accessToken') # токен авторизации

    yield browser, user_data

    browser.quit()
    # удаление пользователя по токену
    user_methods.delete_user(token)
