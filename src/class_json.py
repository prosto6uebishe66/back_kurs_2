from abc import ABC, abstractmethod
import json


class BaseSaver(ABC):

    @abstractmethod
    def read_file(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    def delete_file(self, *args, **kwargs):
        raise NotImplemented


class JSONSaver(BaseSaver):

    def __init__(self, file):
        self.file = file

    def write_data(self, data):
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_file(self):
        with open(self.file, 'w+', encoding='utf-8') as file:
            file.truncate(0)

    def read_file(self, *args, **kwargs):
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
