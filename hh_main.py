from locale import currency
from sys import api_version
import requests
from pprint import pprint
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
    response = requests.get(url,params=payload)
    response.raise_for_status()
    return response.json()


def get_statistics_languages(languages):
    languages_statistics = {}
    for language in languages:
        languages_statistics[language] = get_statistics_vacancies(language)
    pprint(languages_statistics)


def predict_rub_salary(from_salary=None, to_salary=None):
    if  from_salary and to_salary:
        average_salary = from_salary + to_salary / 2
    elif from_salary:
        average_salary = from_salary * 1.2
    elif to_salary:
        average_salary = to_salary * 0.8
    return average_salary


def get_statistics_vacancies(language):
    all_salary = []
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
        
            all_salary.append(predict_rub_salary(salary_from, salary_to))
    if all_salary:
        average_salary = int(sum(all_salary) / len(all_salary))
    else:
        average_salary = None
    
    vacancies_statistics = {
        "vacancies_found": vacancies["found"],
        "vacancies_processed": len(all_salary),
        "average_salary": average_salary
    }
    return vacancies_statistics
     

def main():
    languages = [
        "Python",
        "Java",
        "Javascript",
        "C",
        "Ruby",
        "PHP",
        "Shell",
        "Scala",
        "Swift",
        "TypeScript"
    ]
    get_statistics_languages(languages)
    

if __name__ == "__main__":
    main()
    