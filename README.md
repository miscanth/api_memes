![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)


# API-приложение для работы с коллекцией мемов


## Описание проекта



### Ключевые возможности приложения:

Приложение состоит из двух сервисов: сервис с публичным API с бизнес-логикой и сервис для работы с медиа-файлами, для этого используется S3-совместимое хранилище (MinIO).  


## Используемые технологии

Это полностью рабочий проект, бэкенд-приложение которого создано на базе **FastAPI**.
Для запуска FastAPI использован ASGI-сервер — **Uvicorn**.

К проекту подключены следующие библиотеки:

* Эндпоинты FastAPI настроены на приём JSON при помощи классов **Pydantic**.
* Для работы с env-файлами подключена библиотека **python-dotenv**.
* На этапе разработки использована база данных **PostgreSQL**.
* Для асинхронного подключения к SQLite установлен драйвер **asyncpg**.
* Работа с базой организована через **SQLAlchemy**.
* К проекту так же подключено **ORM SQLAlchemy**.
* Для миграций подключена библиотека **Alembic**.


## Как работать с API:

Полный список эндпоинтов с примерами запросов доступны в документации по следующим адресам:

В формате Swagger:

```
http://127.0.0.1:8000/docs
```
В формате ReDoc:
```
http://127.0.0.1:8000/redoc
```


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке: 
```
git clone git@github.com:miscanth/api_memes.git
```
Cоздать и активировать виртуальное окружение: 
```
python3.9 -m venv venv 
```
* Если у вас Linux/macOS 

    ```
    source venv/bin/activate
    ```
* Если у вас windows 
 
    ```
    source venv/scripts/activate
    ```
```
python3.9 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить проект в режиме разработки:

```
uvicorn app.main:app --reload
```

## Примеры запросов:


## Разработчик (исполнитель):
👩🏼‍💻 Юлия: https://github.com/miscanth