import unittest

from src.utils import filter_vacancies_by_keywords, get_top_n_by_salary


class Vacancy:
    def __init__(self, title, company, salary):
        self.title = title
        self.company = company
        self.salary = salary


class TestVacancySorter(unittest.TestCase):
    def setUp(self):
        self.vacancies = [
            Vacancy("Software Engineer", "Tech Corp", 150000),
            Vacancy("Data Scientist", "Finance Co", 120000),
            Vacancy("Product Manager", "E-commerce Inc", 180000),
            Vacancy("DevOps Engineer", "Cloud Services", 110000),
            Vacancy("UX Designer", "Design Studio", 140000)
        ]

    def test_empty_input(self):
        self.assertEqual(get_top_n_by_salary([], 1), [])

    def test_single_input(self):
        result = get_top_n_by_salary([self.vacancies[0]], 1)
        self.assertEqual(result, [self.vacancies[0]])

    def test_default_output(self):
        result = get_top_n_by_salary(self.vacancies, 3)
        expected_result = sorted(self.vacancies, key=lambda x: x.salary)[-3:]
        self.assertEqual(result, expected_result)

    def test_custom_N(self):
        result = get_top_n_by_salary(self.vacancies, 2)
        expected_result = sorted(self.vacancies, key=lambda x: x.salary)[-2:]
        self.assertEqual(result, expected_result)


def test_filter_vacancies(list_vacancies):
    keywords = ["JS", "Golang"]

    filtered_vacancies = filter_vacancies_by_keywords(list_vacancies, keywords)

    expected = ['Фронтенд разработчик', 'Backend-разработчик']
    actual = [vacancy.name for vacancy in filtered_vacancies]
    assert actual == expected


def test_no_keywords(list_vacancies):
    empty_keywords = []

    result = filter_vacancies_by_keywords(list_vacancies, empty_keywords)

    assert result == list_vacancies
