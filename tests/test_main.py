import pytest
import json

from back_kurs_2.Config import NEW_VACANCIES_PATH
from src.class_hh import HeadHunter
from src.class_json import JSONSaver
from src.function import create_list_obj, sort_salary_from
from back_kurs_2.main import user_interaction, clear_file


def test_headhunter_search():
    hh = HeadHunter()
    vacancy_from_hh = hh.get_vacansies("Python developer")
    assert len(vacancy_from_hh) > 0
    saving_vac = JSONSaver(NEW_VACANCIES_PATH)
    saving_vac.write_data(vacancy_from_hh)

def test_saving_vacancies():
    saving_vac = JSONSaver(NEW_VACANCIES_PATH)
    with open(NEW_VACANCIES_PATH, 'r') as f:
        saved_vacancies = json.load(f)
    assert len(saved_vacancies) > 0


