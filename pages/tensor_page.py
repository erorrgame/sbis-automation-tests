from .base_page import BasePage
from selenium.webdriver.common.by import By
from typing import List, Tuple

class TensorPage(BasePage):
    POWER_IN_PEOPLE_BLOCK = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")
    MORE_DETAILS_LINK = (By.XPATH, "//div[contains(@class, 'tensor_ru-Index__block4-content')]//a[text()='Подробнее']")
    WORK_SECTION = (By.XPATH, "//div[contains(@class, 'tensor_ru-container tensor_ru-section tensor_ru-About__block3')]//h2[text()='Работаем']/ancestor::div[contains(@class, 'tensor_ru-container tensor_ru-section tensor_ru-About__block3')]")
    IMAGE_SELECTOR = "img.tensor_ru-About__block3-image"

    def is_power_in_people_block_present(self) -> bool:
        """Проверка наличия блока "Сила в людях"."""
        self.scroll_to_element(self.POWER_IN_PEOPLE_BLOCK)
        return self.find_element(self.POWER_IN_PEOPLE_BLOCK).is_displayed()

    def click_more_details(self) -> None:
        """Клик на ссылку 'Подробнее'."""
        self.find_element(self.MORE_DETAILS_LINK).click()

    def get_timeline_image_sizes(self) -> List[Tuple[str, str]]:
        """Получение размеров изображений в разделе 'Работаем'."""
        self.scroll_to_element(self.WORK_SECTION)
        work_section = self.find_element(self.WORK_SECTION)
        images = work_section.find_elements(By.CSS_SELECTOR, self.IMAGE_SELECTOR)
        return [(img.get_attribute("width"), img.get_attribute("height")) for img in images]

    def scroll_to_element(self, locator: Tuple[str, str]) -> None:
        """Прокрутка к элементу по локатору."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)