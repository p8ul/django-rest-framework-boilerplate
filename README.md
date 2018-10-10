## django-rest-framework-boilerplate
Simple boilerplate for django & django rest framework

[![Build Status](https://travis-ci.org/p8ul/stackoverflow-lite-client.svg?branch=develop)](https://travis-ci.org/p8ul/stackoverflow-lite-client)
[![Coverage Status](https://coveralls.io/repos/github/p8ul/django-rest-framework-boilerplate/badge.svg?branch=master)](https://coveralls.io/github/p8ul/django-rest-framework-boilerplate?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/e066442f75f4bc3f5269/maintainability)](https://codeclimate.com/github/p8ul/django-rest-framework-boilerplate/maintainability)

### Installation
If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python (here)[python.org].

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv
Then, Git clone this repo to your PC
    $ git clone https://github.com/p8ul/django-rest-framework-boilerplate
    $ cd django-rest-framework-boilerplate
Create a virtual environment
    $ virtualenv .venv && source .venv/bin/activate
Install dependancies
    $ pip install -r requirements.txt
Make migrations & migrate
    $ python manage.py makemigrations && python manage.py migrate

### Launching the app
    $ python manage.py runserver

### Run Tests
    $ python manage.py test

