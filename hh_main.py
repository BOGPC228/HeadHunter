from predict_rub_salary import predict_rub_salary
import requests
from itertools import count


def get_vacancies(language="Python", page=0, specialization="1.221", city_id="1", period=30):
    url = "https://api.hh.ru/vacancies/"
    payload = {
        "specialization": specialization,
        "area": city_id,
        "period": period,
        "text": language,
        "page": page
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def get_statistics_languages_hh(languages):
    languages_statistics = {}
    for language in languages:
        languages_statistics[language] = get_statistics_vacancies(language)
    return languages_statistics


def get_statistics_vacancies(language):
    all_salaries = []
    for page in count(0):
        vacancies = get_vacancies(language, page)       
        if page >= vacancies['pages']-1:
            break
        for vacancy in vacancies["items"]:
            if not vacancy["salary"]:
                continue
            if not vacancy["salary"]["currency"]=="RUR":
                continue
            salary_from = vacancy["salary"]["from"]
            salary_to = vacancy["salary"]["to"]      
            all_salaries.append(predict_rub_salary(salary_from, salary_to))
    if all_salaries:
        average_salary = int(sum(all_salaries) / len(all_salaries))
    else:
        average_salary = None
    vacancies_statistics = {
        "all_vacancies": vacancies["found"],
        "vacancies_processed": len(all_salaries),
        "average_salary": average_salary
    }
    return vacancies_statistics