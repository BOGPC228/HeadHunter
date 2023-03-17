# Сравниваем вакансии программистов

Модули для сравнивнения вакансии программистов с источников hh.ru и superjob.ru.

## Запуск

Для запуска программы у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите зависимости командой 
```python
    pip install -r requirements.txt
```
- Для загрузки таблиц с hh.ru и superjob.ru запустите команду 
```python
    python3 main.py
```

## Переменные окружения

Часть настроек проекта берётся из переменны окружения. Чтобы её определить, создайте файл `.env` в папке с модулем `super_job.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступна следующая переменная:

- `SUPER_JOB_KEY` — см секретный ключ проекта. [сайт API SuperJob](https://api.superjob.ru/?from_refresh=1). Например: `SUPER_JOB_KEY=v3.r.137311988.275d722fe1ae6ebe22c8f2d957e6c09cc71d6ae4.32693b281d6055f5548d0a46a546a0f866ac96e6`.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
