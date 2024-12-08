import pytest
import requests_mock

from src.class_hh import HeadHunter  # Укажите правильный путь к вашему модулю

# Фикстуры для мока ответа API
vacancies_response = {
    "items": [
        {"id": 1234, "name": "Вакансия 1"},
        {"id": 5678, "name": "Вакансия 2"}
    ],
    "found": 20,
    "pages": 10
}


# Тестовый кейс
def test_get_vacancies():
    with requests_mock.Mocker() as m:
        # Мокаем ответ API
        m.get("https://api.hh.ru/vacancies", json=vacancies_response)

        hh = HeadHunter()
        vacancies = hh.get_vacansies(keyword="Тестировщик")

        assert len(vacancies) == 20
        assert vacancies[0]['name'] == "Вакансия 1"
        assert vacancies[1]['name'] == "Вакансия 2"