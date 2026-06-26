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





# Каунтер. Сначала берем значение, потом добавляем и проверяем что увеличился
# Тест на добавление ингредиентов будет параметризованный
# В Firefox невидимого layout нет
# Создать пользователя можно через API
# Сиблинги скинули в чат, можно через них сделать регистрацию, чтобы победить два одинаковых локатора

# В задании с восстановлением пароля требуется проверить только переход на окно с вводом чисел из email, ничего вводить не надо

# Как проверить глаз пароля. Находим локатор когда глаз закрыт, находим элемент. Кликаем. Проверяем, что появился элемент со статусом active. Как я понял после этого мо
# можно кликать на глаз. У глаза обновляется класс на открытый глаз (обновится класс - input__placeholder-focused)
# Забираем локатор с active и вставляем в метод is_displayed. И этот метод пихаем в ассерт и проверяем что тру. Проверили отображение при клике на глазик
# Значение пароля не позволяет провести проверку. Корректная проверка через изменение класса

# На страницу личного кабинета можно перейти по URL, чтобы обойти layout

# Иногда после клика нужен perform, чтобы обычный клик отработал