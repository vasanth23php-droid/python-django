Django frame work setup

1. git init

2. git clone https://github.com/vasanth23php-droid/python-django.git

3. python -m venv moviecollection

4. moviecollection\Scripts\activate

5. py -m pip install Django==6.0

6. python -m pip install --upgrade pip 

7. django-admin startproejct movieinfo

8. python manage.py startapp movielist_app

9. python manage.py runserver

10. add the app into setting.py in proejct folder

	INSTALLED_APPS = [
    			'django.contrib.admin',
			'django.contrib.auth',
			'django.contrib.contenttypes',
			'django.contrib.sessions',
			'django.contrib.messages',
			'django.contrib.staticfiles',
			'movielist_app'
			]

11. Create the Model file

12. python manage.py makemigrations

13. python manage.py migrate

14. 


