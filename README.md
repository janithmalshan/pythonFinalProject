# pythonFinalProject

## Job offer portal
This project has an advance search which you can find specific job related to the skills


----------------------------------------------------
django-admin startproject hollymovies
python manage.py - to view list of commands
projectname manage.py ??
goto project directory
python manage.py runserver

python manage.py startapp viewer - make app

project ekak athule app godak thiyenna pulwn - python manage.py startapp polls
register app in settings.py
-- installed apps -> viewer



model eka hadala
make migration

python manage.py shell
from viewer.models import Genre
Genre.objects.create(name="Romance")
Genre.object.create(name="Drama")


python manage.py createsuperuser

models eke change krat passe
- makemigrate and migrate aaniwaryayi

add data
======
from datetime import datetime
new_job = Job(title='Designer UI', publish_date=datetime.fromisoformat('2021-07-07'))
new_job.save()



===
adding a page - 3 steps
create view - view.py
create template in template folder
setup URL - url.py

======
register on admin.py