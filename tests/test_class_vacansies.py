import pytest

from src.class_vacansies import Vacansy
import pytest

@pytest.fixture
def vacancy():
    return Vacansy(
        title= "Тестировщик",
        city= "Москва",
        salary_to= 50000,
        salary_from= 70000,
        description= "Описание вакансии",
        link= "https://example.com/job"
    )

@pytest.fixture
def another_vacancy():
    return Vacansy(
        title="Разработчик",
        city="Санкт-Петербург",
        salary_to=60000,
        salary_from=90000,
        description="Другое описание вакансии",
        link=" https://another.example.com/job"
    )

class TestVacansy:
    def test_init(self, vacancy):
        assert vacancy.title == "Тестировщик"
        assert vacancy.city == "Москва"
        assert vacancy.salary_from == 50000
        assert vacancy.salary_to == 70000
        assert vacancy.description == "Описание вакансии"
        assert vacancy._link == "https://example.com/job"

    def test_str(self, vacancy):
        expected_string = (
            "Вакансия Тестировщик ГородМосква"
            "Зарплата от 50000 до 70000"
            "Ссылкаhttps://example.com/job"
        )

        assert str(vacancy) == expected_string

    def test_repr(self, vacancy):
        expected_repr = (
            "Тестировщик, Москва, 50000,"
            "70000, Описание вакансии, https://example.com/job"
        )

        assert repr(vacancy) == expected_repr

    def test_title_data(self, vacancy):
        assert vacancy.title_data == "Тестировщик"

    def test_city_data(self, vacancy):
        assert vacancy.city_data == "Москва"

    def test_link_data(self, vacancy):
        assert vacancy._link == "https://example.com/job"

    def test_ne(self, vacancy, another_vacancy):
        assert vacancy != another_vacancy
