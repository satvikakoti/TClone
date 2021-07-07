# <module-path> is the relative path to the folder that contains the module
# that contains wsgi.py; <module> is the name of the folder containing wsgi.py.
gunicorn --bind=0.0.0.0 --timeout 1800 --workers=1 --chdir TeamsCloneProject/ TeamsCloneProject.wsgi
