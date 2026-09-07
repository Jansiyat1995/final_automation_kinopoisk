import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__wait = WebDriverWait(driver, 15)

    @allure.step("Открыть Кинопоиск")
    def go(self):
        self.__driver.get("https://www.kinopoisk.ru/")

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

    @allure.step("Ввести название фильма в поиск")
    def search_movie(self, movie_name: str):
        search_input = self.__wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    'input[placeholder="Фильмы, сериалы, персоны"]'
                )
            )
        )
        search_input.clear()
        search_input.send_keys(movie_name)
        search_input.send_keys(Keys.ENTER)

    @allure.step("Выбрать фильм из результатов поиска")
    def select_movie(self, movie_name: str):
        movie = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f'//span[normalize-space()="{movie_name}"]'
                )
            )
        )
        movie.click()

    @allure.step("Получить название фильма")
    def get_movie_title(self, movie_name: str) -> str:
        title = self.__wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f'//span[normalize-space()="{movie_name}"]'
                )
            )
        )
        return title.text

    @allure.step("Открыть раздел «Фильмы»")
    def open_movies(self):
        movies = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    'a[href="/lists/categories/movies/1/"]'
                )
            )
        )
        movies.click()

    @allure.step("Открыть раздел «Жанры»")
    def open_genres(self):
        genres = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    'a[data-test-id="next-link"]'
                    '[href="/lists/categories/movies/8/"]'
                )
            )
        )
        genres.click()

    @allure.step("Выбрать жанр «Комедии»")
    def select_comedy(self):
        comedy = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    'a[data-test-id="next-link"]'
                    '[href="/lists/movies/genre--comedy/?b=top"]'
                )
            )
        )
        comedy.click()

    @allure.step("Выбрать фильм «Холоп 2»")
    def select_holop_2(self):
        movie = self.__wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    'a[href="/film/5047468/"]'
                )
            )
        )
        movie.click()

    @allure.step("Получить название фильма «Холоп 2»")
    def get_holop_2_title(self) -> str:
        title = self.__wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                'span[data-tid="75209b22"]'
            )
        )
    )
        return title.text

    @allure.step("Проверить наличие фильма")
    def is_movie_present(self, movie_name: str) -> bool:
        movies = self.__driver.find_elements(
            By.XPATH,
            f'//span[normalize-space()="{movie_name}"]'
        )
        return len(movies) > 0
