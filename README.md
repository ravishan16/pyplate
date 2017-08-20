Flask Microservice App
======================

Simple Flask App, SQLAchemy, SQLite, Gunicorn, Docker, Microservice, Python

[![Build Status](https://travis-ci.org/ravishan16/FlaskApp.svg?branch=master)](https://travis-ci.org/ravishan16/FlaskApp)[![Code Climate](https://codeclimate.com/github/ravishan16/FlaskApp/badges/gpa.svg)](https://codeclimate.com/github/FlaskApp/CountByAlexa)[![Test Coverage](https://codeclimate.com/github/ravishan16/FlaskApp/badges/coverage.svg)](https://codeclimate.com/github/ravishan16/FlaskApp)[![Issue Count](https://codeclimate.com/github/ravishan16/FlaskApp/badges/issue_count.svg)](https://codeclimate.com/github/ravishan16/FlaskApp)

Setup DB
========

python manage.py db init python manage.py db migrate python manage.py db upgrade

Run Flask Server Local
======================

python manage.py db runserver

docker build -t flaskapi-docker:0.0.1 . docker run -d -p 8000:4000 flaskapi-docker:0.0.1 docker ps -all
