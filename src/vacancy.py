from typing import Any


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "url", "area", "salary", "description")

    def __init__(self, name, url, area, salary, description) -> None:
        self.name = name
        self.url = url
        self.area = area
        self.salary = salary
        self.description = description
        self.__validate()

    def __validate(self) -> None:
        """Метод валидации входных данных"""
        if not self.salary:
            self.salary = 0

        if not self.description:
            self.description = "Описание отсутствует"

        if not self.area:
            self.area = "Регион не указан"

    def __str__(self) -> str:
        if self.salary == 0:
            self.salary = "Не указана"
            return f"{self.name}: {self.description}, Регион:{self.area}, Зарплата: {self.salary}, Ссылка: {self.url}"
        else:
            return f"{self.name}: {self.description}, Регион:{self.area}, Зарплата: {self.salary}, Ссылка: {self.url}"

    @classmethod
    def cast_to_object_list(cls, vacancies) -> list[Any]:
        """Метод преобразовывает набор данных из JSON в список объектов"""
        vacancies_list = []
        for item in vacancies:
            name = item.get("name")
            url = item.get("alternate_url")
            area = item.get("area").get("name")
            if item["salary"] is None:
                salary = 0
            else:
                salary = item.get("salary").get("from")
            description = item.get("snippet").get("requirement")
            vacancies_list.append(cls(name, url, area, salary, description))
        return vacancies_list

    def __lt__(self, other):
        """Метод сравнивает между собой по зарплате и возвращает вакансию с большей зарплатой"""
        if self.salary < other.salary:
            return True
        else:
            return False