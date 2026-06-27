import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BasePage:

    def wait_for_load(self, driver, element):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((element)))

    def wait_element_until_invisibility(self, driver, element):
        WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located(element))

    def wait_for_change_text_of_element(self, driver, element, text):
        try:
            WebDriverWait(driver, 10).until(lambda d: d.find_element(*element).text != text)
        except TimeoutException:
            raise TimeoutException("Текст не изменился за отведённое время")

    def click_button(self, driver, element):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((element)))
        driver.find_element(*element).click()

    def element_is_displayed(self, driver, element):
        self.wait_for_load(driver, element)
        return driver.find_element(*element).is_displayed()
    
    def element_is_not_displayed(self, driver, element):
        self.wait_element_until_invisibility(driver, element)
        return (not driver.find_element(*element).is_displayed())

    def get_text_attribute(self, driver, element):
        return driver.find_element(*element).text
    
    def get_id_order_elements_list(self, driver, element):
        return driver.find_elements(*element)
    
    def find_element_with_wait(self, driver, element):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((element)))
        return driver.find_element(*element)
    
    def click_virt_mouse(self, driver, locator):
        action = ActionChains(driver)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element = driver.find_element(*locator)
        action.click(on_element=element).perform()

    @allure.step('Перетаскиваем ингредиент в зону заказа')
    def my_drag_and_drop(self, driver, locator_from, locator_to):
        elem_from = self.find_element_with_wait(driver, locator_from) # находим элемент который хотим перетащить
        elem_to = self.find_element_with_wait(driver, locator_to) # находим элемент на который хотим перетащить
        # drag_and_drop - встроенный метод selenium ActionChains (РАБОТАЕТ ТОЛЬКО В CHROME)
        # передавать нужно не локаторы, а сами веб-элементы
        actions = ActionChains(driver)
        actions.drag_and_drop(elem_from, elem_to).perform() # perform() - отпустить

    @allure.step('Перетаскиваем ингредиент в зону заказа')
    def drag_and_drop_firefox(self, driver, locator_from, locator_to):
        self.wait_for_load(driver, locator_from)
        self.wait_for_load(driver, locator_to)
        element_from = driver.find_element(*locator_from)
        element_to = driver.find_element(*locator_to)
        self.driver.execute_script("""
                                var source = arguments[0];
                                var target = arguments[1];
                                var evt = document.createEvent("DragEvent");
                                evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                source.dispatchEvent(evt);
                                evt = document.createEvent("DragEvent");
                                evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                target.dispatchEvent(evt);
                                evt = document.createEvent("DragEvent");
                                evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                target.dispatchEvent(evt);
                                evt = document.createEvent("DragEvent");
                                evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                target.dispatchEvent(evt);
                                evt = document.createEvent("DragEvent");
                                evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                source.dispatchEvent(evt);
                                """, element_from, element_to)
        
    def send_keys(self, driver, element, comment):
        driver.find_element(*element).send_keys(comment)

    def get_current_url(self, driver):
        return driver.current_url

    







    def move_element(self, locator_source, locator_target):
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()

    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()
