def get_top_n_by_salary(vacancies: list, n: int) -> list:
    """Функция возвращает топ N вакансий по зарплате (N запрашивается у пользователя)"""
    return sorted(vacancies, key=lambda x: x.salary)[-n:]


def filter_vacancies_by_keywords(vacancies: list, keywords: list) -> list:
    """
    Функция фильтрует вакансии по ключевым словам
    """
    if not keywords:
        return vacancies

    keyword_set = set(keywords)

    return [vacancy for vacancy in vacancies if any(keyword in vacancy.description for keyword in keyword_set)]


def print_vacancies(vacancies: list) -> None:
    """Функция выводит в консоль список вакансий"""
    for vacancy in vacancies:
        print(vacancy)
