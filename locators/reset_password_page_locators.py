from selenium.webdriver.common.by import By


RECOVERING = [By.XPATH, "//h2[text()='Восстановление пароля']"]
PASSWORD_FOR_RECOVER = [By.CSS_SELECTOR, "input[type='password']"]
EYE_BTN = [By.CSS_SELECTOR, "div.input__icon.input__icon-action svg"]
FIELD_EYE_CLOSE = [By.CSS_SELECTOR, "div.input.pr-6.pl-6.input_type_password.input_size_default"]
FIELD_ACTIVE_EYE_OPEN = [By.CSS_SELECTOR, "div.input.pr-6.pl-6.input_type_text.input_size_default.input_status_active"]
LABEL_EYE_CLOSE = [By.XPATH, "//label[@class='input__placeholder text noselect text_type_main-default' and text()='Пароль']"]
LABEL_ACTIVE_EYE_OPEN = [By.XPATH, "//label[@class='input__placeholder text noselect text_type_main-default input__placeholder-focused' and text()='Пароль']"]
