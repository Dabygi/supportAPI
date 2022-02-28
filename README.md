# supportAPI

Это django-rest-framework приложение технической поддержки на основе тикетов 
с аутентификацией на основе JSON Web Token и возможностью добавления комментариев.

###### Написано с использованием:

Django, django-rest-framework, simpleJWT, django-filters, celery, redis, PostgreSQL, Docker, Docker-Compose.
Для код стайла flake8.


### Приложение включает в себя:

1. Регистрация, логин, логаут (c применением Python Social Auth);
2. Профиль пользователя:
* Возможность изменния и сохранения всех личных данных.
* Возможность просмотра чужого профиля и его тикетов.

3. Модель тикета (CRUD)

* Создание тикета (Create)

* Чтение тикета (Read)

* Редактирование тикета (Update)

* Удаление тикета (Delete)

4. Модель комментариев

* создание комментария
* добавление комментария к нужному тикету.

Как запустить проект у себя?

1 - git clone https://github.com/Dabygi/supportAPI.git

2 - запросить у владельца проекта https://www.linkedin.com/in/artem-gluhotorenko .env файл

3 - .env файл положить в корневую папку проекта supportAPI

4 - выбрать интерпретатор из supportAPI --> docker-compose.yml  Service Web

5 - Запустить проект

6 - Находясь в директории, где лежит Makefile прописать:
make mkm --> make m  --> make load

7 - Либо локально:

  - python3 -m venv ДиректорияВиртуальногоОкружения
  - source ДиректорияВиртуальногоОкружения/bin/activate
  - Перейти в директорию supportAPI
  - pip install -r requirements.txt
  - Проверьте соединение с БД (postgresql), либо создайте базу
  - python manage.py migrate
  - python manage.py runserver
