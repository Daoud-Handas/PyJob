Contains all the needed command to set up the project.\
The website is accessible at : http://127.0.0.1:8000/

## Setup virtual environment 
**create venv :**
`python -m venv ./venv`

**start venv :**
`./venv/Scripts/activate`

**stop venv :**
`deactivate`

**update requirements.txt :**
`pip freeze > requirements.txt`

**install from requirements :**
`python -m pip install -r requirements.txt`

**installed packages :**
* `python -m pip install Django`

## Django command
**create Django project :**
`django-admin startproject PyJob_Website`

**create app**
`python manage.py startapp Jobs`

**create migration :**
`python manage.py makemigrations`

**run migration :**
`python manage.py migrate`

**run server :**
`python manage.py runserver`

**pour tester en mode shell :**
`python manage.py shell`



