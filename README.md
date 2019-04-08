Flask Microservice App
======================

Simple Flask App, SQLAchemy, SQLite, Gunicorn, Docker, Microservice, Python

[![Build Status](https://travis-ci.org/ravishan16/FlaskApp.svg?branch=master)](https://travis-ci.org/ravishan16/FlaskApp)[![Code Climate](https://codeclimate.com/github/ravishan16/FlaskApp/badges/gpa.svg)](https://codeclimate.com/github/FlaskApp/CountByAlexa)[![Test Coverage](https://codeclimate.com/github/ravishan16/FlaskApp/badges/coverage.svg)](https://codeclimate.com/github/ravishan16/FlaskApp)[![Issue Count](https://codeclimate.com/github/ravishan16/FlaskApp/badges/issue_count.svg)](https://codeclimate.com/github/ravishan16/FlaskApp)
[![Docker Hub](https://hub.docker.com/public/images/logos/mini-logo.svg)](https://hub.docker.com/r/ravishan/flaskapp/)

Setup DB
========

``` python
python manage.py db init 
python manage.py db migrate 
python manage.py db upgrade
```

Run Flask Server Local
======================

``` python
python manage.py db runserver
```

## Build Docker

``` shell
docker build -t flaskapi-docker:0.0.1 . 
```

## Run Docker image

``` shell
docker run -d -p 8000:4000 --name flaskapp flaskapi-docker:0.0.1 
```

## Docker Pull and Run 

``` shell
docker run -d -p 8000:4000 --name flaskapp ravishan/flaskapp
```

##  Check Docker Status

``` shell
docker ps -all
```

## Check Logs

``` shell
docker logs -tf flaskapp


2017-08-31T18:49:51.237387132Z Running Production Application
2017-08-31T18:49:51.493803743Z [2017-08-31 18:49:51 +0000] [1] [INFO] Starting gunicorn 19.7.1
2017-08-31T18:49:51.496746605Z [2017-08-31 18:49:51 +0000] [1] [INFO] Listening at: http://0.0.0.0:4000 (1)
2017-08-31T18:49:51.496764705Z [2017-08-31 18:49:51 +0000] [1] [INFO] Using worker: sync
2017-08-31T18:49:51.496767590Z [2017-08-31 18:49:51 +0000] [9] [INFO] Booting worker with pid: 9
2017-08-31T18:49:51.602635517Z [2017-08-31 18:49:51 +0000] [14] [INFO] Booting worker with pid: 14
2017-08-31T18:49:51.678074435Z [2017-08-31 18:49:51 +0000] [15] [INFO] Booting worker with pid: 15
2017-08-31T18:49:51.748691820Z [2017-08-31 18:49:51 +0000] [20] [INFO] Booting worker with pid: 20
``` 

## Smoke Test

``` shell
curl -i http://localhost:8000/main/users

HTTP/1.1 200 OK
Server: gunicorn/19.7.1
Date: Thu, 31 Aug 2017 18:47:39 GMT
Connection: close
Content-Type: application/json
Content-Length: 18

{
  "users": []
}
```


-- Ravishankar Sivsasubramaniam
