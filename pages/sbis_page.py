import time
import os

from .base_page import BasePage
from selenium.webdriver.common.by import By

class SbisPage(BasePage):
    CONTACTS_LINK = (By.XPATH, "//a[contains(@href, '/contacts')]")
    TENSOR_BANNER = (By.XPATH, "//img[contains(@alt, 'Разработчик системы СБИС — компания «Тензор»')]")

    REGION_LABEL = (By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser__text.sbis_ru-link")
    PARTNERS_LIST = (By.CSS_SELECTOR, '.sbisru-Contacts-List__name')

    LOCAL_VERSIONS_LINK = (By.LINK_TEXT, "Скачать локальные версии")
    PLUGIN_LINK = (By.XPATH, '//div[contains(@class, "controls-TabButton__caption") and contains(text(), "СБИС Плагин")]')
    PAGE_WINDOWS = (By.CSS_SELECTOR, 'span.sbis_ru-DownloadNew-innerTabs__title--default')
    WEB_INSTALLER_LINK = (By.XPATH, '//h3[contains(text(), "Веб-установщик")]/ancestor::div[contains(@class, "sbis_ru-DownloadNew-flex")]/descendant::a[contains(@class, "sbis_ru-DownloadNew-loadLink__link")]')
    PLUGIN_SIZE = (By.XPATH, '//h3[contains(text(), "Веб-установщик")]/ancestor::div[contains(@class, "sbis_ru-DownloadNew-flex")]/descendant::a[contains(@class, "sbis_ru-DownloadNew-loadLink__link")]')

    def go_to_contacts(self) -> None:
        """Переход на страницу 'Контакты'. Сценарий 1."""
        self.find_element_visibility(self.CONTACTS_LINK).click()

    def click_tensor_banner(self) -> None:
        """Клик на баннер Тензор. Сценарий 1."""
        self.find_element_visibility(self.TENSOR_BANNER).click()

    def get_region(self) -> str:
        """Получение текущего региона."""
        region_element = self.find_element_visibility(self.REGION_LABEL)
        return region_element.text

    def get_partners_list(self) -> list:
        """Получение списка партнеров."""
        partners_elements = self.find_elements_visibility(self.PARTNERS_LIST)
        partners_texts = [element.text for element in partners_elements]
        return partners_texts

    def change_region(self, region: str) -> None:
        """Изменение региона."""
        self.find_element(self.REGION_LABEL).click()
        REGION_ITEM = (By.XPATH, f'//li[@class="sbis_ru-Region-Panel__item"]//span[text()="{region}"]')
        self.find_element_clickable(REGION_ITEM).click()
        region_without_number = ' '.join(region.split(' ')[1:])
        self.wait_for_change(self.REGION_LABEL, region_without_number)

    def navigate_to_local_versions(self) -> None:
        """Переход к разделу 'Скачать локальные версии' в футере."""
        footer_link = self.find_element_clickable(self.LOCAL_VERSIONS_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_link)
        footer_link.click()

    def download_plugin(self) -> None:
        """Скачивание плагина."""
        plugin_link = self.find_element_visibility(self.PLUGIN_LINK)
        plugin_link.click()
        self.find_element_clickable(self.PAGE_WINDOWS).click()
        self.find_element_clickable(self.WEB_INSTALLER_LINK).click()
        time.sleep(7)

    def get_plugin_size(self) -> float:
        """Получение размера плагина с сайта."""
        size_text = self.find_element_clickable(self.PLUGIN_SIZE).text
        size_in_mb = size_text.split('(')[-1].split()[1].replace('МБ', '').replace(',', '.')
        return float(size_in_mb)

    def is_file_downloaded(self, filename: str) -> bool:
        """Проверка, что файл скачан."""
        file_path = os.path.join(os.getcwd(), filename)
        return os.path.isfile(file_path)

    def get_file_size_in_mb(self, filepath: str) -> float:
        """Получение размера файла в МБ."""
        size_in_bytes = os.path.getsize(filepath)
        size_in_mb = size_in_bytes / (1024 * 1024)
        return round(size_in_mb, 2)


