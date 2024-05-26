import requests
from src.abstract_classes import HHAbstract
from src.editing_vacancies import EditingVacancies


class GetApiHH(HHAbstract):
    """Класс для работы с API HeadHunter и получения вакансий."""

    def __init__(self, text=""):
        """
        Инициализация объекта GetApiHH.

        Параметры:
            text (str): Текст для поиска вакансий.
        """
        self.url = "https://api.hh.ru/vacancies"
        self.text = text

    def get_vacancy(self) -> list[EditingVacancies]:
        """
        Получение списка вакансий.

        Возвращает:
            list[EditingVacancies]: Список объектов, представляющих вакансии.
        """
        param_get = {"text": self.text, "per_page": 100, "area": 1,
                     "order_by": "relevance", "only_with_salary": True}
        response = requests.get(url=self.url, params=param_get)
        if response.status_code == 200:
            return self.convert_to_vacancy(response.json())
        else:
            print(f"Ошибка при запросе к API HH: {response.status_code}")
            return []

    def convert_to_vacancy(self, data) -> list[EditingVacancies]:
        """
        Преобразование данных о вакансиях в объекты EditingVacancies.

        Параметры:
            data (dict): Словарь данных о вакансиях.

        Возвращает:
            list[EditingVacancies]: Список объектов вакансий.
        """
        return [EditingVacancies(name=i["name"],
                                 alternate_url=i["alternate_url"],
                                 salary_from=int(self.__recursion("from", i.get("salary", "Пусто"), message=0)),
                                 salary_to=self.__recursion("to", i.get("salary", "Пусто"), ""),
                                 currency=self.__recursion("currency", i.get("salary", "Пусто"), ""),
                                 requirement=self.__recursion('requirement', i.get("snippet"), "Не написали"),
                                 experience=self.__recursion("name", i["experience"], "**"))
                for i in data['items']]

    def __recursion(self, key, dict_obj, message):
        """
        Рекурсивный поиск значения ключа в словаре.

        Параметры:
            key (str): Ключ для поиска.
            dict_obj (dict): Словарь для поиска значения ключа.
            message (str): Сообщение, возвращаемое в случае отсутствия ключа.

        Возвращает:
            str: Значение ключа или сообщение об его отсутствии.
        """
        if dict_obj is None:
            return f'{message}'
        if key in dict_obj:
            if dict_obj[key] is None:
                return f'{message}'
            return dict_obj[key]
        for k, v in dict_obj.items():
            if isinstance(v, dict):
                result = self.__recursion(key, v, message)
                if result is not None:
                    return result
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, dict) and key in item:
                        return self.__recursion(key, item, message)
        return f'Ключ "{key}" не найден в объекте'
