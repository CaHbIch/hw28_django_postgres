FROM python:3.10-slim

# установить рабочий каталог
WORKDIR /code

#установить зависимости
COPY pyproject.toml .
RUN pip install poetry
RUN POETRY_VIRTUALENVS_CREATE=false poetry install

#скопировать проект
COPY . .

#Запускать интерпретатор python по умолчанию
ENTRYPOINT ["sh", "entrypoint.sh"]