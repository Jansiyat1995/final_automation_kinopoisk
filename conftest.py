import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    """Запускает браузер Chrome перед тестом и закрывает после него."""
    with allure.step("Открыть и настроить браузер"):
        chrome_options = Options()
        chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )
        chrome_options.page_load_strategy = "eager"

        browser = webdriver.Chrome(options=chrome_options)
        browser.set_page_load_timeout(120)
        browser.maximize_window()

    yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()
