[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=white&color=009688)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=red&color=800000)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=alembic&logoColor=white&color=556B2F)](https://alembic.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=pydantic&logoColor=white&color=3776AB)](https://docs.pydantic.dev/)
[![Uvicorn](https://img.shields.io/badge/-Uvicorn-464646?style=flat&logo=uvicorn&logoColor=white&color=000000)](https://www.uvicorn.org/)
[![FastAPI Users](https://img.shields.io/badge/-FastAPI__Users-464646?style=flat&logo=fastapi&logoColor=white&color=607D8B)](https://frankie567.github.io/fastapi-users/)

[![Pytest](https://img.shields.io/badge/-Pytest-464646?style=flat&logo=pytest&logoColor=white&color=6A1B9A)](https://docs.pytest.org/)
[![Flake8](https://img.shields.io/badge/-Flake8-464646?style=flat&logo=flake8&logoColor=white&color=4B0082)](https://flake8.pycqa.org/)
[![Isort](https://img.shields.io/badge/-Isort-464646?style=flat&logo=python&logoColor=white&color=708090)](https://pycqa.github.io/isort/)
[![Dotenv](https://img.shields.io/badge/-python__dotenv-464646?style=flat&logo=python-dotenv&logoColor=white&color=2E8B57)](https://pypi.org/project/python-dotenv/)

# 🐾 QR Kot

Благотворительный фонд поддержки котиков.

---

## Описание

**QR Kot** — это благотворительный фонд помощи котикам. Сервис позволяет создавать проекты по сбору средств и делать пожертвования. Пожертвования автоматически распределяются между проектами по принципу **FIFO**.

Проект включает:

- 🔐 Авторизацию и регистрацию пользователей  
- 👥 Управление ролями и правами доступа  
- 📝 Создание проектов с указанием необходимой суммы  
- 💸 Создание пожертвований  
- 🔁 Автоматическое распределение пожертвований по активным проектам

Документация API: **"openapi.json"**

## Установка

Клонирование и установка зависимостей:

```bash
# клонируйте репозиторий.
git clone https://github.com/VitsVi/cat_charity_fund
# перейдите в папку проекта.
cd cat_charity_fund
# создайте и запустите виртуальное окружение.
python -m venv venv
source venv/bin/activate  # или .\venv\Scripts\activate на Windows
# установите зависимости проекта.
pip install -r requirements.txt
```

Далее создайте и заполните **.env** файл в корне проекта:
```.env
APP_TITLE=QR Kot
APP_DESCRIPTION=Благотворительный фонд поддержки котиков
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
```

## Запуск

В корневой директории проекта выполните команду:

```bash
uvicorn app.main:app --reload
```

## Эндпоинты

**Swagger** для просмотра и работы с доступными эндпоинтами:
```
http://127.0.0.1:8000/docs
```

### Автор

[VitsVi](https://github.com/VitsVi)

Почта: jigulsky.vitalik@yandex.ru
