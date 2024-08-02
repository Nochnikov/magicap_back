FROM python:3.11-slim-bullseye

RUN mkdir code
WORKDIR code
ADD requirements.txt /code/

RUN pip install -r requirements.txt
ADD . /code/

CMD gunicorn mysite.wsgi:application -b 0.0.0.0:8000






