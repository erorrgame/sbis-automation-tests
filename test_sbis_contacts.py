from pages.sbis_page import SbisPage
from conftest import log_assert_result


def test_change_region_and_verify(browser):
    browser.get("https://sbis.ru/")

    # Перейти в раздел "Контакты"
    sbis_page = SbisPage(browser)
    sbis_page.go_to_contacts()

    # Проверить текущий регион и наличие списка партнеров
    current_region = sbis_page.get_region()
    partners_list_before = sbis_page.get_partners_list()
    log_assert_result("г. Москва" in current_region,
                      f"Регион '{current_region}' совпал с 'г. Москва'",
                      f"Регион '{current_region}' не совпал с 'г. Москва'")
    assert "г. Москва" in current_region
    log_assert_result(len(partners_list_before) > 0,
                      f"Получен список партнеров - ({len(partners_list_before)}) {partners_list_before}!",
                      f"Cписок партнеров не получен, либо пустой!")
    assert len(partners_list_before) > 0

    # Изменить регион на Камчатский край
    sbis_page.change_region("41 Камчатский край")

    # Проверить новый регион, изменение списка партнеров и URL/title страницы
    current_region = sbis_page.get_region()
    partners_list_after = sbis_page.get_partners_list()
    log_assert_result("Камчатский край" in current_region,
                      f"Регион изменен на '{current_region}' и совпадает с 'Камчатский край'!",
                      f"Регион изменен на '{current_region}' и не совпадает с 'Камчатский край'!")
    assert "Камчатский край" in current_region
    log_assert_result(partners_list_before != partners_list_after,
                      f"Лист партнеров изменен на '{partners_list_after}'!",
                      f"Лист партнеров не изменился - '{partners_list_after}'")
    assert partners_list_before != partners_list_after
    log_assert_result("41-kamchatskij-kraj" in browser.current_url,
                      f"Ссылка изменена и содержит '41-kamchatskij-kraj' - {browser.current_url}!",
                      f"Ссылка не корректно изменена и не содержит '41-kamchatskij-kraj' - {browser.current_url}!")
    assert "41-kamchatskij-kraj" in browser.current_url
    log_assert_result("Камчатский край" in browser.title,
                      f"Регион 'Камчатский край' отобразился в titel - {browser.title}",
                      f"Регион 'Камчатский край' не отобразился в titel - {browser.title}")
    assert "Камчатский край" in browser.title
