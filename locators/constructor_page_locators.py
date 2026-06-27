from selenium.webdriver.common.by import By

CONSTRUCT_BURGER_HEADER_BTN_ACTIVE = [By.XPATH, "//li/a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']"]
ORDERS_FEED_HEADER_BTN = [By.XPATH, "//li[@class='undefined ml-2']/a[@class='AppHeader_header__link__3D_hX']"]
INVISIBLE_LAYOUT = [By.XPATH, "//div.[@class='Modal_modal_overlay__x2ZCr']"]

INGR_KRATOR_BUN = [By.XPATH, "//p[text()='Краторная булка N-200i']/parent::a"]
INGR_KRATOR_BUN_COUNTER = [By.XPATH, "//p[text()='Краторная булка N-200i']/parent::a/div[@class='counter_counter__ZNLkj counter_default__28sqi']/p"]
INGR_FLUOR_BUN = [By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a"]
INGR_FLUOR_BUN_COUNTER = [By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a/div[@class='counter_counter__ZNLkj counter_default__28sqi']/p"]
INGR_SPICY_SAUCE = [By.XPATH, "//p[text()='Соус Spicy-X']/parent::a"]
INGR_SPICY_SAUCE_COUNTER = [By.XPATH, "//p[text()='Соус Spicy-X']/parent::a/div[@class='counter_counter__ZNLkj counter_default__28sqi']/p"]

DETAILS_WINDOW = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 div.Modal_modal__container__Wo2l_"]
DETAILS_WINDOW_TITLE = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 div.Modal_modal__container__Wo2l_ div h2"]
DETAILS_WINDOW_KRATOR_BUN = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 div.Modal_modal__container__Wo2l_ div p"]
DETAILS_WINDOW_CLOSED = [By.CSS_SELECTOR, "section.Modal_modal__P3_V5 div.Modal_modal__container__Wo2l_"]
CROSS_BTN = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 div.Modal_modal__container__Wo2l_ button svg"]

BASKET_ZONE = [By.CSS_SELECTOR, "section.BurgerConstructor_basket__29Cd7.mt-25 ul"]

SIGN_IN_ACCOUNT = [By.XPATH, "//button[text()='Войти в аккаунт']"]
PLACE_ORDER_BTN = [By.XPATH, "//button[text()='Оформить заказ']"]

ID_ORDER_WINDOW_LABEL = [By.XPATH, "//p[text()='идентификатор заказа']"]
ID_CREATED_ORDER = [By.XPATH, "//p[text()='идентификатор заказа']/parent::div/h2"]

PERSONAL_ACCOUNT = [By.XPATH, "//p[text()='Личный Кабинет']/parent::a"]
    