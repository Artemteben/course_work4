import json
import os

from src.abstract_classes import AbstractVacancy
from src.editing_vacancies import EditingVacancies


class SaveToFormatFile(AbstractVacancy):
    def __init__(self, filename="data/my_vacancy.json"):
        """
        Инициализирует объект класса SaveToFormatFile.

        Args:
            filename (str, optional): Имя файла для сохранения вакансий.
                По умолчанию "data/my_vacancy.json".
        """
        self.filename = filename

    def save_vacancy_to_file(self, json_obj):
        """
        Сохраняет вакансии в JSON файл.

        Args:
            self.json_obj (list): Список объектов, представляющих вакансии.

        Raises:
            FileNotFoundError: Если файл не найден.
        """
        existing_data = []
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf8") as file:
                try:
                    existing_data = json.load(file)
                except json.decoder.JSONDecodeError:
                    "Пусто"

        existing_data.extend([value_json.to_json() for value_json in json_obj])

        with open(self.filename, "w", encoding="utf8") as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)

    def read_vacancy_from_file(self):
        """
        Читает вакансии из JSON файла.
        """
        file_path = "data/my_vacancy.json"
        with open(file_path, 'r', encoding="utf8") as file:
            json_file = json.load(file)
            return [EditingVacancies(name=i['name'], alternate_url=i['alternate_url'],
                                     salary_from=i['salary_from'],
                                     salary_to=i['salary_to'], requirement=i['requirement'],
                                     experience=i['experience'],
                                     currency=i['currency']) for i in json_file]

    def del_vacancy_from_file(self):
        """
        Удаляет содержимое файла.
        """
        with open(self.filename, "w", encoding="utf8") as file:
            file.seek(0)
            file.truncate()
