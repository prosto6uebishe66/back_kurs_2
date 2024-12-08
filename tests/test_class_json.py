import json
import os
import tempfile
import pytest

from src.class_json import JSONSaver

class TestJSONSaver:
    def setup_method(self):
        # Создаём временный файл для тестирования
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.temp_dir.name, 'test.json')
        self.saver = JSONSaver(self.file_path)

    def teardown_method(self):
        # Удаляем временный файл после завершения теста
        self.temp_dir.cleanup()

    def test_write_data(self):
        # Запись данных в файл
        data = {'key1': 'value1', 'key2': 'value2'}
        self.saver.write_data(data)

        # Чтение данных из файла
        with open(self.file_path, 'r', encoding='utf-8') as file:
            actual_data = json.load(file)

        # Сравнение записанных и считанных данных
        assert actual_data == data

    def test_delete_file(self):
        # Запись данных в файл
        data = {'key1': 'value1', 'key2': 'value2'}
        self.saver.write_data(data)

        # Очистка файла
        self.saver.delete_file()

        # Чтение данных из очищенного файла
        with open(self.file_path, 'r', encoding='utf-8') as file:
            actual_data = file.read()

        # Проверка, что файл пуст
        assert actual_data == ''

    def test_read_file_empty(self):
        # Чтение данных из несуществующего файла
        actual_data = self.saver.read_file()

        # Проверка, что возвращается пустой словарь
        assert actual_data == {}

    def test_read_file_nonempty(self):
        # Запись данных в файл
        data = {'key1': 'value1', 'key2': 'value2'}
        self.saver.write_data(data)

        # Чтение данных из файла
        actual_data = self.saver.read_file()

        # Сравнение записанных и считанных данных
        assert actual_data == data
