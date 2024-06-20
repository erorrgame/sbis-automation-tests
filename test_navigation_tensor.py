from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from conftest import log_assert_result


def test_tensor_navigation(browser):
    browser.get("https://sbis.ru/")

    # Перейти в раздел "Контакты"
    sbis_page = SbisPage(browser)
    sbis_page.go_to_contacts()

    # Кликнуть по баннеру Тензор
    sbis_page.click_tensor_banner()

    # Переключиться на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # Проверить блок "Сила в людях"
    tensor_page = TensorPage(browser)
    result_block_power_in_people = tensor_page.is_power_in_people_block_present()
    log_assert_result(result_block_power_in_people,
                      f"Блок 'Сила в людях' найден!",
                      f"Блок 'Сила в людях' не найден!")
    assert result_block_power_in_people, "Блок 'Сила в людях' не найден"

    # Кликнуть на "Подробнее" в блоке "Сила в людях"
    tensor_page.click_more_details()
    log_assert_result(browser.current_url == "https://tensor.ru/about",
                      f"URL совпал: '{browser.current_url}' == 'https://tensor.ru/about'",
                      f"URL не соответствует ожиданиям {browser.current_url} != 'https://tensor.ru/about'")
    assert browser.current_url == "https://tensor.ru/about", "URL не соответствует ожиданиям"

    # Проверить, что изображения хронологии имеют одинаковые размеры
    image_sizes = tensor_page.get_timeline_image_sizes()
    result_image_sizes = all(size == image_sizes[0] for size in image_sizes)
    log_assert_result(result_image_sizes,
                      f"Все изображения имеют одинаковые размеры: {image_sizes}!!",
                      f"Не все изображения имеют одинаковые размеры: {image_sizes}!")
    assert result_image_sizes, "Не все изображения имеют одинаковые размеры"