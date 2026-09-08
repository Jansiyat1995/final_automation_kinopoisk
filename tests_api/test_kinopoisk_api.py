import os

import allure
import requests
from dotenv import load_dotenv


load_dotenv()

BASE_URL = "https://api.poiskkino.dev/v1.4/movie"
API_KEY = os.getenv("KINOPOISK_API_KEY")

HEADERS = {
    "x-api-key": API_KEY,
}


@allure.feature("Поиск фильмов")
@allure.title("Поиск фильмов по году")
@allure.description("Проверка получения фильмов за 2020 год.")
def test_movie_year_2020():
    params = {
        "year": 2020,
    }

    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        params=params,
        timeout=30,
    )

    assert response.status_code == 200
    assert response.json()["docs"]


@allure.feature("Поиск фильмов")
@allure.title("Поиск фильмов по жанру")
@allure.description("Проверка поиска фильмов жанра фантастика.")
def test_movie_genre_fantasy():
    params = {
        "genres.name": "фантастика",
    }

    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        params=params,
        timeout=30,
    )

    assert response.status_code == 200
    assert response.json()["docs"]


@allure.feature("Поиск фильмов")
@allure.title("Поиск фильмов по рейтингу")
@allure.description("Проверка поиска фильмов с рейтингом от 5 до 10.")
def test_movie_rating_5_10():
    params = {
        "rating.kp": "5-10",
    }

    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        params=params,
        timeout=30,
    )

    assert response.status_code == 200
    assert response.json()["docs"]


@allure.feature("Валидация параметров")
@allure.title("Ошибка при некорректном годе")
@allure.description("Проверка обработки некорректного значения года.")
def test_invalid_year():
    params = {
        "year": 30215,
    }

    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        params=params,
        timeout=30,
    )

    assert response.status_code == 400


@allure.feature("Авторизация")
@allure.title("Ошибка при неверном API-ключе")
@allure.description("Проверка отклонения запроса с неверным API-ключом.")
def test_invalid_token():
    headers = {
        "x-api-key": "invalid_token",
    }

    response = requests.get(
        BASE_URL,
        headers=headers,
        timeout=30,
    )

    assert response.status_code == 401
