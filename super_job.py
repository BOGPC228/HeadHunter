from predict_rub_salary import predict_rub_salary
import requests
from itertools import count


def get_vacancies(super_job_key, page=0, language="Python", id="4", id_catalog=48, period=30):
    headers = {"X-Api-App-Id": super_job_key}
    url = "https://api.superjob.ru/2.0/vacancies/"
    params = {
        "page": page,
        "town": id,
        "catalogues": id_catalog,
        "keyword": language,
        "period": period
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def get_statistics_languages_job(languages, super_job_key):
    languages_statistics = {}
    for language in languages:
        languages_statistics[language] = get_vacancies_professional(language, super_job_key)
    return languages_statistics


def get_vacancies_professional(language, super_job_key):
    all_salary = []
    for page in count(0):
        vacancies = get_vacancies(super_job_key, page, language)

        for vacancy in vacancies['objects']:
            if not vacancy["payment_from"] and not vacancy["payment_to"]:
                continue
            if not vacancy["currency"] == "rub":
                continue
            salary_from = vacancy["payment_from"]
            salary_to = vacancy["payment_to"]

            all_salary.append(predict_rub_salary(salary_from, salary_to))

        if not vacancies['more']:
            break
    if all_salary:
        average_salary = int(sum(all_salary) / len(all_salary))
    else:
        average_salary = None


    vacancies_statistics = {
        "all_vacancies": vacancies["total"],
        "vacancies_processed": len(all_salary),
        "average_salary": average_salary
    }
    return vacancies_statistics