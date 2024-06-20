from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        """Поиск элемента в DOM."""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_element_visibility(self, locator, time=10):
        """Поиск элемента visibility."""
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def find_element_clickable(self, locator, time=10):
        """Поиск элемента clickable."""
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def find_elements(self, locator, time=10):
        """Поиск нескольких элементов в DOM."""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def find_elements_visibility(self, locator, time=10):
        """Поиск нескольких элементов visibility."""
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))

    def wait_for_change(self, locator, expected_region, time=10):
        """Ожидание смены локатора."""
        WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, expected_region))
        return
