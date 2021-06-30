web: gunicorn TeamsCloneProject.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
worker: python manage.py runworker channel_layer
