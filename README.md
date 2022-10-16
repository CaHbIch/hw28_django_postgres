## Проект готов к локальному запуску
Запустить базу данных postgres:  docker-compose up --build -d


### Создание fixture и загрузка данных

Зайти в папку "ad/datasets" (там лежат файлы csv с данными)

Выполнить 'python3 load_csv_to_json.py' (получает данные из файлов csv, преобразует в json и помещает в папку с fixtures)

### Миграции
Необходимо создать миграцию "./manage.py makemigrations"  и накатить миграцию "./manage.py migrate"

Вернитесь в папку проекта и загрузите данные в БД выполните « ./manage.py loaddata ad.json ».
Выполнить «python3 manage.py loaddata category.json»

### Доступные маршруты и методы

/ad/ - GET, POST
/ad/3 - GET
/cat/ - GET, POST
/cat/3/ - GET