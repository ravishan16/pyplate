# FlaskApp
Simple Flask App, SQLAchemy, SQLite, CherryPy



# Setup DB

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Run Flask Server Local

python manage.py db runserver



docker build -t flaskapi-docker:0.0.1 .
docker run -d  -p 8000:4000 flaskapi-docker:0.0.1
docker ps -all