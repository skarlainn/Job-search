from src.job_search import SearchVacancies
from src.vacancy import Vacancy
from src.utils import filter_vacancies_by_keywords, get_top_n_by_salary, \
    print_vacancies
from src.file_worker import JSONSWorker


# Функция для взаимодействия с пользователем
def user_interaction():
    print("Вас приветствует программа поиска вакансий с сайта hh.ru")
    search_query = input("Введите поисковый запрос: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий разделяя пробелом: ").split()
    top_n = int(input("Введите количество вакансий для вывода в топ N по зарплате: "))
    print("Идет поиск вакансий...")

    hh_api = SearchVacancies()
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    filtered_vacancies = filter_vacancies_by_keywords(vacancies_list, filter_words)
    if top_n:
        top_vacancies = get_top_n_by_salary(filtered_vacancies, top_n)
    else:
        print("Вы не ввели число вакансий, будет выведено 10 вакансий")
        top_n = 10
        top_vacancies = get_top_n_by_salary(filtered_vacancies, top_n)

    user_response = input("Сохранить вакансии в файл? (yes/no): ").lower()
    if user_response == "yes":
        filename = input("Введите название файла: ")
        if filename:
            file = f"{filename}.json"
            result = JSONSWorker(file)
            result.save_to_file(top_vacancies)
            print(f"Вакансии успешно сохранены в файл -> {file}")
        else:
            result = JSONSWorker()
            result.save_to_file(top_vacancies)
            print(f"Вакансии сохранены в файл по умолчанию -> vacancies.json")
    else:
        print("Вакансии не сохранены")

    if top_vacancies:
        print(f"Найдено {len(top_vacancies)} вакансий")
        print_vacancies(top_vacancies)
    else:
        print("Ничего не найдено по Вашим критериям")


if __name__ == "__main__":
    user_interaction()