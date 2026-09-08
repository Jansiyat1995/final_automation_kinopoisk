import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver
        self.__wait = WebDriverWait(driver, 15)

    @allure.step("Открыть Кинопоиск")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Закрыть всплывающее окно")
    def close_popup(self):
        close_button = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    'button[aria-label="Закрыть коммуникацию"]'
                )
            )
        )
        close_button.click()

    @allure.step("Нажать кнопку «Войти» на Кинопоиске")
    def click_login(self):
        login_button = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//button[contains(., "Войти")]'
                )
            )
        )
        login_button.click()

    @allure.step("Нажать «Ещё»")
    def click_more(self):
        more_button = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    '[data-testid="split-add-user-more-button"]'
                )
            )
        )
        more_button.click()

    @allure.step("Выбрать «Войти по логину»")
    def click_login_by_login(self):
        login_by_login = self.__wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[data-testid="menu-option-switchToLogin"]')))
        login_by_login.click()

    @allure.step("Ввести логин или email")
    def enter_login(self, login: str):
        login_input = self.__wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    'input[data-testid="text-field-input"]'
                    '[aria-label="Логин или email"]'
                )
            )
        )
        login_input.clear()
        login_input.send_keys(login)

    @allure.step("Нажать «Войти» после ввода логина")
    def click_login_after_login(self):
        login_button = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    '[data-testid="split-add-user-next-login"]'
                )
            )
        )
        login_button.click()

    @allure.step("Нажать «Войти с паролем»")
    def click_login_with_password(self):
        password_button = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    '[data-testid="password-btn"]'
                )
            )
        )
        password_button.click()

    @allure.step("Ввести пароль")
    def enter_password(self, password: str):
        password_input = self.__wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    'input[data-testid="text-field-input"]'
                    '[autocomplete="current-password"]'
                )
            )
        )
        password_input.clear()
        password_input.send_keys(password)

    @allure.step("Нажать «Далее»")
    def click_next(self):
        next_button = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    '[data-testid="password-next"]'
                )
            )
        )
        next_button.click()

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url
