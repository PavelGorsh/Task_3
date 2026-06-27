from selenium.webdriver.common.by import By

CONSTRUCT_BURGER_HEADER_BTN = [By.XPATH, "//li/a[@class='AppHeader_header__link__3D_hX']"]
ORDERS_FEED_HEADER_BTN_ACTIVE = [By.XPATH, "//li[@class='undefined ml-2']/a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']"]

UPPER_ORDER = [By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[1]/a"]
UPPER_ORDER_TITLE = [By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[1]/a/h2"]
DETAILS_WINDOW_CONTAIN = [By.XPATH, "//p[text()='Cостав']"] # В коде программы буква С написана латиницей
DETAILS_WINDOW_TITLE = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 div div h2"]
ID_ORDER_LIST_FROM_ORDERS_FEED = [By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r.mb-6>a.OrderHistory_link__1iNby>div.OrderHistory_textBox__3lgbs.mb-6>p.text.text_type_digits-default"]
ORDERS_QUANTITY_ALL_TIME = [By.XPATH, "//p[text()='Выполнено за все время:']/parent::div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
ORDERS_QUANTITY_TODAY = [By.XPATH, "//p[text()='Выполнено за сегодня:']/parent::div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
ID_ORDER_LIST_FROM_COMPLITED = [By.CSS_SELECTOR, "li.text.text_type_digits-default.mb-2"]
ID_ORDER_LIST_FROM_IN_WORK = [By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li"]
