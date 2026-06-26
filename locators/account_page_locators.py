from selenium.webdriver.common.by import By


PROFILE_BTN = [By.XPATH, "//a[text()='Профиль']"]
PROFILE_BTN_ACTIVE = [By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and @href='/account/profile']"]
HISTORY_BTN = [By.XPATH, "//a[text()='История заказов']"]
HISTORY_BTN_ACTIVE = [By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and @href='/account/order-history']"]