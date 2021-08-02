FROM python:3.8-slim-buster

ADD weather.py .

RUN pip install flask

RUN pip install requests

COPY weather.py weather.py

COPY templates templates

ENTRYPOINT FLASK_APP=weather.py flask run --host=0.0.0.0