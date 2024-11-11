from abc import ABC, abstractmethod
import requests


class BaseHH(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacansies(self, *args, **kwargs):
        pass


class HeadHunter(BaseHH):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'area': 113}
        self.vacancies = []

    def get_vacansies(self, keyword) -> list:
        self.params['text'] = keyword
        while self.params.get('page') != 10:
            response = requests.get(self.url, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        return self.vacancies