from abc import ABC, abstractmethod


class HHAbstract(ABC):

    @abstractmethod
    def get_vacancy(self):
        pass


class AbstractVacancy(ABC):
    """Абстрактный базовый класс для работы с вакансиями."""

    @abstractmethod
    def saver(self):
        """
        Абстрактный метод для сохранения вакансии в файл.

        Метод должен быть реализован в подклассах.

        """
        pass

    @abstractmethod
    def reader(self):
        """
        Абстрактный метод для чтения вакансии из файла.

        Метод должен быть реализован в подклассах.

        """
        pass

    @abstractmethod
    def delf(self):
        """
        Абстрактный метод для удаления вакансии из файла.

        Метод должен быть реализован в подклассах.

        """
        pass
