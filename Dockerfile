from python:3.6.4

add requirements.txt /app/
workdir /app
run pip install -r requirements.txt

add . /app

expose 5000

env HOST=0.0.0.0
cmd python app.py
