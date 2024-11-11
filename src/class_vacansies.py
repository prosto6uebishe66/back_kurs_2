from abc import ABC, abstractmethod

from src.class_json import BaseSaver


class BaseVacancy(ABC):

    __slots__ = ('title', 'city', 'salary_from', 'salary_to', 'description', 'link')

    @abstractmethod
    def __init__(self,title, city, salary_from, salary_to, description, link ):
        self.title = title
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self._link = link

    @abstractmethod
    def __str__(self):
        pass

class Vacansy(BaseVacancy):

    title: str
    city: str
    salary_to: int
    salary_from: int
    description: str
    link: str

    def __init__(self, title: str, city: str, salary_to: int, salary_from: int, description: str, link: str):

        super().__init__(title, city, salary_to, salary_from, description, link)

    def __repr__(self):
        return (f"{self.title}, {self.city}, {self.salary_from},"
                f"{self.salary_to}, {self.description}, {self._link}")

    def __str__(self):
        return (f"Вакансия {self.title} "
                f"Город{self.city}"
                f"Зарплата от {self.salary_from} до {self.salary_to}"
                f"Ссылка{self._link}")

    @property
    def title_data(self):
        if self.title is not None:
            return  self.title
        else:
            return "Error"


    @property
    def city_data(self):
        if self.city is not None:
            return self.city
        else:
            return "Not city found"

    @property
    def link_data(self):
        if self.link is None:
            return self._link
        else:
            return "Link is not found"

    def __lt__(self, other):
        if self.salary_from is None or other.salary_from is None:
            return False
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        if self.salary_from is None or other.salary_from is None:
            return False
        return self.salary_from > other.salary_from
