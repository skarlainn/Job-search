import json
import os

import pytest
from src.vacancy import Vacancy

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../tests/data_test.json")
abs_file_path = os.path.abspath(rel_file_path)


@pytest.fixture
def vacancy_test():
    return Vacancy("Фронтенд разработчик", "https://hh.ru/vacancy/109570768", "Ташкент", 2000000,
                   "Знания HTML, CSS, JS, Jquery.")


@pytest.fixture
def vacancy_test_2():
    return Vacancy("Фронтенд разработчик", "https://hh.ru/vacancy/109570768", None, None, None)


@pytest.fixture
def json_data():
    with open(abs_file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data


@pytest.fixture
def list_vacancies():
    return [
        Vacancy("Фронтенд разработчик", "https://hh.ru/vacancy/109570768", "Ташкент", 2000000,
                "Знания HTML, CSS, JS, Jquery."),
        Vacancy("React Front-End Developer (Frontend разработчик)", "https://hh.ru/vacancy/109792373",
                "Ташкент", 10000,
                "Базовые знания HTML / CSS / JavaScript. React / React Native. English (на уровне понимания технических текстов). Русский язык (для общения). "),
        Vacancy("Backend-разработчик", "https://hh.ru/vacancy/110131426",
                "Ташкент", 40000,
                "Уверенное владение языком Golang. -Знакомство с Docker. -Понимание CI/CD и облачных платформ (AWS, GCP или Azure). -Отличные навыки решения...")
    ]
