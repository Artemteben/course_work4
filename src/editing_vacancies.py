class EditingVacancies:
    """Класс, представляющий информацию о вакансии."""

    def __init__(self, name: str, alternate_url: str, salary_from: int,
                 salary_to: int, currency: str,
                 requirement: str, experience: str):
        """
        Инициализация объекта вакансии.

        Параметры:
            name (str): Название вакансии.
            alternate_url (str): Альтернативный URL для вакансии.
            salary_from (int): Минимальная заработная плата.
            salary_to (int): Максимальная заработная плата.
            currency (str): Валюта заработной платы.
            requirement (str): Требования к соискателю.
            experience (str): Опыт работы.
        """
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.requirement = requirement
        self.experience = experience

    def __str__(self) -> str:
        """
        Представление объекта в виде строки.

        Возвращает:
            str: Строковое представление объекта.
        """
        return (f"Профессия: {self.name},"
                f" заработная плата: {self.salary_from} - {self.salary_to} {self.__currency}"
                f" Опыт работы: {self.experience.lower()}")

    @property
    def __currency(self) -> str:
        """
        Определение символа валюты.

        Возвращает:
            str: Символ валюты.
        """
        match self.currency:
            case 'RUR':
                return 'рублей.'
            case 'EUR':
                return 'евро.'
            case 'USD':
                return 'долларов США.'

    def __lt__(self, other):
        """
        Сравнение вакансий по минимальной заработной плате.

        Параметры:
            other (EditingVacancies): Другая вакансия.

        Возвращает:
            bool: True, если зп текущей вакансии меньше,
            чем у другой, иначе False.
        """
        return self.salary_from < other.salary_from

    def to_json(self) -> dict:
        """
        Представление вакансии в виде словаря JSON.

        Возвращает:
            dict: Словарь с информацией о вакансии.
        """
        return {"name": self.name,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "currency": self.currency,
                "requirement": self.requirement,
                "experience": self.experience,
                "alternate_url": self.alternate_url}
