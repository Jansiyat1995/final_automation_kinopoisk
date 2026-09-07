import allure

from page.SearchPage import SearchPage


@allure.title("Поиск фильма по названию")
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_movie(browser):

    search_page = SearchPage(browser)

    with allure.step("Открыть Кинопоиск"):
        search_page.go()

    with allure.step("Закрыть всплывающее окно"):
        search_page.close_popup()

    with allure.step("Найти «Унесённые призраками»"):
        search_page.search_movie("Унесённые призраками")

    with allure.step("Выбрать фильм"):
        search_page.select_movie("Унесённые призраками")

    with allure.step("Проверить название фильма"):
        title = search_page.get_movie_title(
            "Унесённые призраками"
        )
        assert title == "Унесённые призраками"


@allure.title("Выбор фильма через каталог")
@allure.feature("Каталог фильмов")
@allure.severity(allure.severity_level.CRITICAL)
def test_select_movie_from_catalog(browser):

    search_page = SearchPage(browser)

    with allure.step("Открыть Кинопоиск"):
        search_page.go()

    with allure.step("Закрыть всплывающее окно"):
        search_page.close_popup()

    with allure.step("Открыть раздел «Фильмы»"):
        search_page.open_movies()

    with allure.step("Открыть раздел «Жанры»"):
        search_page.open_genres()

    with allure.step("Выбрать жанр «Комедии»"):
        search_page.select_comedy()

    with allure.step("Выбрать фильм «Холоп 2»"):
        search_page.select_holop_2()

    with allure.step("Проверить название фильма"):
        title = search_page.get_holop_2_title()
        assert title == "Холоп 2 (2023)"


@allure.title("Поиск несуществующего фильма")
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.NORMAL)
def test_search_nonexistent_movie(browser):

    search_page = SearchPage(browser)

    with allure.step("Открыть Кинопоиск"):
        search_page.go()

    with allure.step("Закрыть всплывающее окно"):
        search_page.close_popup()

    with allure.step("Ввести название несуществующего фильма"):
        search_page.search_movie("ФильмКоторогоНет999999")

    with allure.step("Проверить отсутствие фильма"):
        assert not search_page.is_movie_present(
            "ФильмКоторогоНет999999"
        )


@allure.title("Проверка отсутствия фильма другого жанра")
@allure.feature("Каталог фильмов")
@allure.severity(allure.severity_level.NORMAL)
def test_movie_of_another_genre_not_in_comedy_catalog(browser):

    search_page = SearchPage(browser)

    with allure.step("Открыть Кинопоиск"):
        search_page.go()

    with allure.step("Закрыть всплывающее окно"):
        search_page.close_popup()

    with allure.step("Открыть раздел «Фильмы»"):
        search_page.open_movies()

    with allure.step("Открыть раздел «Жанры»"):
        search_page.open_genres()

    with allure.step("Выбрать жанр «Комедии»"):
        search_page.select_comedy()

    with allure.step(
        "Проверить отсутствие «Унесённых призраками»"
    ):
        assert not search_page.is_movie_present(
            "Унесённые призраками"
        )
