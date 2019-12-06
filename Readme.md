# Django photo API

## Установка без docker и reverse proxy

1. Настроить конфигурацию, указав параметры подключения к БД в .env файле:  
``cp app/photoapi/.env.example app/photoapi/.env``
2. Выполнить установку зависимостей:  
``pip install -r requirements.txt``
3. Запустить миграции:   
``cd app && python manage.py migrate``
4. Создать админа для админки:  
``cd app && python manage.py createsuperuser``

## Установка через docker
1. Настроить конфигурацию, указав параметры подключения к БД в .env файле:  
``cp app/photoapi/.env.example app/photoapi/.env``
2. Собрать образ:  
``docker-compose build``
3. Запустить все контейнеры:  
``docker-compose up -d``
4. Запустить миграции:   
``docker exec -it web python manage.py migrate``
5. Создать админа для админки:  
``docker exec -it web python manage.py createsuperuser``
