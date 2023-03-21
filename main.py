from hh_main import get_statistics_languages_hh
from super_job import get_statistics_languages_job
import os
from dotenv import load_dotenv
from terminaltables import AsciiTable


def create_table(languages_statistics, title):
    table_options = [
      ['Язык программирования', 'Вакансий найдено',  'Вакансий обработано', 'Средняя зарплата']
    ]
    for language, language_statistics in languages_statistics.items():
        table_options.append([language, language_statistics["all_vacancies"],
                            language_statistics["vacancies_processed"],
                            language_statistics["average_salary"] or 0])
    table= AsciiTable(table_options, title)
    return table.table


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
    super_job_title = "SuperJob Moscow"
    headhunter_title = "HeadHunter Moscow"
    load_dotenv()
    super_job_key = os.getenv("SUPER_JOB_KEY")
    languages_statistics_hh = get_statistics_languages_hh(languages)
    languages_statistics_job = get_statistics_languages_job(languages, super_job_key)
    print(create_table(languages_statistics_hh, headhunter_title))
    print(create_table(languages_statistics_job, super_job_title))
    

if __name__ == "__main__":
    main()