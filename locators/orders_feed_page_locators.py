from selenium.webdriver.common.by import By

CONSTRUCT_BURGER_HEADER_BTN = [By.XPATH, "//li/a[@class='AppHeader_header__link__3D_hX']"]
ORDERS_FEED_HEADER_BTN_ACTIVE = [By.XPATH, "//li[@class='undefined ml-2']/a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']"]

UPPER_ORDER = [By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[1]/a"]
UPPER_ORDER_TITLE = [By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[1]/a/h2"]
DETAILS_WINDOW_CONTAIN = [By.XPATH, "//p[text()='Cостав']"] # В коде программы буква С написана латиницей
DETAILS_WINDOW_TITLE = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 div div h2"]

    