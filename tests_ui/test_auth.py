import os

import allure
from dotenv import load_dotenv

from page.AuthPage import AuthPage


load_dotenv()


@allure.title("Авторизация в Кинопоиске по логину и паролю")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_authentication(browser):

    login = os.getenv("KINOPOISK_LOGIN")
    password = os.getenv("KINOPOISK_PASSWORD")

    assert login, "Не указан KINOPOISK_LOGIN в файле .env"
    assert password, "Не указан KINOPOISK_PASSWORD в файле .env"

    auth_page = AuthPage(browser)

    with allure.step("Открыть Кинопоиск"):
        auth_page.go()

    with allure.step("Закрыть всплывающее окно"):
        auth_page.close_popup()

    with allure.step("Нажать «Войти»"):
        auth_page.click_login()

    with allure.step("Нажать «Ещё»"):
        auth_page.click_more()

    with allure.step("Выбрать «Войти по логину»"):
        auth_page.click_login_by_login()

    with allure.step("Ввести логин или email"):
        auth_page.enter_login(login)

    with allure.step("Нажать «Войти»"):
        auth_page.click_login_after_login()

    with allure.step("Нажать «Войти с паролем»"):
        auth_page.click_login_with_password()

    with allure.step("Ввести пароль"):
        auth_page.enter_password(password)

    with allure.step("Нажать «Далее»"):
        auth_page.click_next()

    with allure.step("Проверить успешную авторизацию"):
        assert "kinopoisk.ru" in auth_page.get_current_url()
