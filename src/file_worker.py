import json
import os
from typing import Any, Dict, List

from config import DATA_PATH
from src.api_class import FileWorker
from src.vacancy import Vacancy


class JSONSWorker(FileWorker):
    """Класс сохраняет данные в JSON-файл"""

    def __init__(self, filename="vacancies.json") -> None:
        self.__filename = filename
        self.file_path = os.path.join(DATA_PATH, self.__filename)

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([], file)

    def _load_data(self) -> List[Dict[str, Any]]:
        """Чтение данных из JSON-файла"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def _save_data(self, data: List[Dict[str, Any]]) -> None:
        """Сохранение данных в JSON-файл"""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def save_to_file(self, vacancies: List[Vacancy]) -> None:
        """Метод сохраняющий список вакансий в JSON-файл"""
        data = self._load_data()
        for vacancy in vacancies:
            data.append(
                {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "area": vacancy.area,
                    "salary": vacancy.salary,
                    "description": vacancy.description,
                }
            )
        self._save_data(data)

    def get_vacancies(self) -> List[Vacancy]:
        """Метод получает список вакансий из файла"""
        data = self._load_data()
        return [Vacancy(**item) for item in data]

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод добавляет вакансии в существующий файл"""
        data = self._load_data()
        data.append(
            {
                "name": vacancy.name,
                "url": vacancy.url,
                "area": vacancy.area,
                "salary": vacancy.salary,
                "description": vacancy.description,
            }
        )
        self._save_data(data)

    def delete_vacancy(self, vacancy_name: str) -> None:
        """Метод удаляет выбранную вакансию"""
        data = self._load_data()
        data = [item for item in data if item["name"] != vacancy_name]
        self._save_data(data)
