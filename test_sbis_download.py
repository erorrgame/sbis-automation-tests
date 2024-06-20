from pages.sbis_page import SbisPage
from conftest import log_assert_result


def test_download_plugin(browser):
    plugin_filename = "sbisplugin-setup-web.exe"  # Имя файла, который будет загружен

    browser.get("https://sbis.ru/")
    sbis_page = SbisPage(browser)

    # В Footer'e найти и перейти "Скачать локальные версии"
    sbis_page.navigate_to_local_versions()

    # Скачать СБИС Плагин для Windows
    sbis_page.download_plugin()

    # Убедиться, что плагин скачался
    result_file_download = sbis_page.is_file_downloaded(plugin_filename)
    log_assert_result(result_file_download, f"Файл {plugin_filename} скачался", f"Файл {plugin_filename} не скачался")
    assert result_file_download, "Файл не скачался"

    # Сравнить размер скачанного файла в мегабайтах
    downloaded_file_size = sbis_page.get_file_size_in_mb(plugin_filename)
    expected_size = sbis_page.get_plugin_size()
    log_assert_result(downloaded_file_size == expected_size, f"Размер скачанного файла ({downloaded_file_size} MB) совпадает с указанным на сайте ({expected_size} MB)", f"Размер скачанного файла ({downloaded_file_size} MB) не совпадает с указанным на сайте ({expected_size} MB)")
    assert downloaded_file_size == expected_size, f"Размер скачанного файла ({downloaded_file_size} MB) не совпадает с указанным на сайте ({expected_size} MB)"