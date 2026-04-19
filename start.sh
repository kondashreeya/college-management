
python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn college_deploy.wsgi:application --bind 0.0.0.0:$PORT 