# This is an implementation of a basic async chat server using django-channels and redis.

## All that I have done so far is take the code and implement it.

## If I make updates and build on it, I will update it on further branches!

#### Install

1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate

#### Run

4. docker run -p 6379:6379 -d redis:5
5. python manage.py runserver
