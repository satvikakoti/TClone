web: gunicorn TeamsCloneProject.wsgi
worker: python manage.py runworker channel_layer
release: python manage.py migrate
