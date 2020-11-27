
mkdir templates apps assets assets/static assets/media assets/static/css assets/static/images assets/static/js

touch apps/__init__.py

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate