## Проект готов к локальному запуску

Запустить базу данных c postgres:  docker-compose up -d

### Миграции

Накатить миграцию:

./manage.py migrate

### Загрузка данных в БД :

./manage.py loaddata locations.json'
./manage.py loaddata users.json'
./manage.py loaddata categories.json'
./manage.py loaddata ads.json'

### Для доступа к админке

Пользователь: skypro
пароль: 1234
