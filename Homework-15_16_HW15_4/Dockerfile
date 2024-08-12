# Используем базовый образ Python 3.11
FROM python:3.11

# Устанавливаем переменную окружения для отключения вывода стандартного вывода и ошибок Python в буфер
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем зависимости poetry
RUN curl -sSL https://install.python-poetry.org | python -
COPY poetry.lock pyproject.toml /app/

ENV PATH="${PATH}:/root/.local/bin" \
    POETRY_VIRTUALENVS_CREATE=False \
    PYTHONPATH="${PYTHONPATH}:/opt:/opt/src"

RUN poetry install

# Устанавливаем htop
RUN apt-get update && apt-get install -y htop vim

# Копируем исходный код проекта в контейнер
COPY . .

# Выполняем команду для запуска Django сервера
CMD ["python", "spaceoftanks/manage.py", "runserver", "localhost:8000"]
