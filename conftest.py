import logging
import os
import pytest
from selenium import webdriver

logging.basicConfig(filename='test_results.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('\n\n---------------------------------------------\n')


@pytest.fixture(scope="function")
def browser():
    """Фикстура для инициализации и завершения работы с WebDriver Chrome."""
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('prefs', {
        "download.default_directory": os.getcwd(),  # Установите текущий рабочий каталог для загрузок
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True,  # False может помочь обходить защиту, но использовать с осторожностью
        "safebrowsing.disable_download_protection": True  # Отключает защиту от вредоносных загрузок
    })
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def log_assert_result(result: bool, message_done: str, message_failed: str) -> None:
    """Логирование результата assert в файл лога."""
    if result:
        logging.info(f"Успех! {message_done}")
    else:
        logging.error(message_failed)