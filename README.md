Проверка  
1) Распакуйте проект в папку C:\DZ D8
2) Откройте командную строку и зайдите в директорию проекта:
   - cd C:\DZ D8
3) Создайте виртуальное окружение:
   - python -m venv django
4) Активируйте виртуальное окружение:
   - django\Scripts\activate.bat
5) Установите все необходимые пакеты:
   - pip install -r requirements.txt
6) Выполните следующие команды:
   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py createsuperuser
   - python manage.py runserver

Для того, чтобы сделать деплой на heroku необходимо:
1) Перейти в каталог с проектом:
   - cd C:\DZ D8
2) Выполнить следующие команды:
   - git init
   - git add .
   - git commit -m "initial commit"
   - heroku login
   - heroku create
   - heroku addons:create heroku-postgresql --as DATABASE
   - heroku config:set SECRET_KEY=Ваш_секретный_код
   - heroku config:set DISABLE_COLLECTSTATIC=1
   - git push heroku master
   - heroku config:unset DISABLE_COLLECTSTATIC
   - heroku run python manage.py collectstatic --noinput
   - heroku run python manage.py makemigrations
   - heroku run python manage.py migrate
   - heroku run python manage.py createsuperuser
3) Запускаем приложение:
   - heroku open

   Данный проект находится на https://powerful-falls-58637.herokuapp.com/
   По умолчанию логин и пароль для пользователя-администратора в проекте:
   - Логин: pws_admin
   - Пароль: sf_password
