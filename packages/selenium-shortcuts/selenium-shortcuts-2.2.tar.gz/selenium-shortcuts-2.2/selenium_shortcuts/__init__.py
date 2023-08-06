from selenium.webdriver.common.by import By

class setup:
    '''Shortcut functions for Selenium'''
    def __init__(self, driver, wait_for=10):
        driver.implicitly_wait(wait_for) # Wait X seconds for element to load before raising error
        self.driver = driver
        self.wait_for = wait_for
        
    def find(self, css_selector, attribute=None, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element(By.CSS_SELECTOR, css_selector)
        if attribute:
            attribute = element.get_attribute(attribute)
            return element, attribute
        return element

    def finds(self, css_selector, parent=None, wait_for=None):
        if not parent:
            parent = self.driver
        if wait_for:
            self.driver.implicitly_wait(wait_for)
        elements = parent.find_elements(By.CSS_SELECTOR, css_selector)
        if wait_for:
            self.driver.implicitly_wait(self.wait_for)
        return elements

    def click(self, css_selector, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element(By.CSS_SELECTOR, css_selector)
        element.click()

    def text(self, css_selector, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element(By.CSS_SELECTOR, css_selector)
        return element.text

    def send(self, css_selector, text, clear=False, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element(By.CSS_SELECTOR, css_selector)
        if clear:
            element.clear()
        element.send_keys(text)
    
    def get(self, url, parent=None):
        if not parent:
            parent = self.driver
        if parent.current_url != url:
            parent.get(url)

    def check(self, css_selector, parent=None):
        if not parent:
            parent = self.driver
        self.driver.implicitly_wait(1)
        elements = parent.find_elements(By.CSS_SELECTOR, css_selector)
        self.driver.implicitly_wait(self.wait_for)
        if elements and elements[0].is_displayed():
            return elements
        else:
            return None