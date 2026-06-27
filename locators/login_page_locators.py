from selenium.webdriver.common.by import By


SIGN_IN_EMAIL = [By.XPATH, "//label[text()='Email']/parent::div/input[@class='text input__textfield text_type_main-default']"]
SIGN_IN_PASSWORD = [By.XPATH, "//label[text()='Пароль']/parent::div/input[@class='text input__textfield text_type_main-default']"]
SIGN_IN = [By.XPATH, "//button[text()='Войти']"]
RECOVER_PASSWORD = [By.XPATH, "//a[text()='Восстановить пароль']"]
