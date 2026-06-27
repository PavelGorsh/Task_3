from selenium.webdriver.common.by import By


RECOVERING = [By.XPATH, "//h2[text()='Восстановление пароля']"]
EMAIL_FOR_RECOVER = [By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default"]
RECOVER_BTN = [By.XPATH, "//button[text()='Восстановить']"]
