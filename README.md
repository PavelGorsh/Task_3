## Задание 3: веб-приложение

### Автотесты для проверки UI программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы UI-тесты, покрывающие страницы 'qa-stellarburgers.education-services.ru', 'qa-stellarburgers.education-services.ru/feed', 'qa-stellarburgers.education-services.ru/account/profile'

Создан allure-отчёт

### Структура проекта

- `methods` - пакет, содержащий методы для страниц Stellar Burgers
- `tests` - пакет, содержащий тесты, разделенные по классам: `test_constructor_page.py`, `test_order_feed_page.py`

### Основа для написания автотестов

Фреймворк pytest

### Основа для автоматизации действий с браузером

Фреймворк selenium

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**

>  `$ pytest -v`

**Формирование allure-отчёта**

>  `$ pytest tests/ --alluredir=allure_results`

**Формирование allure-отчёта в формате веб-страницы**

>  `$ allure serve allure_results`

### Документация

URL Stellar Burgers: https://qa-stellarburgers.education-services.ru/
