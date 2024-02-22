FROM python:3.12-slim

WORKDIR /backend

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN apt-get update && apt-get install -y vim

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /backend/src/backend

CMD gunicorn --bind 0.0.0.0:8000 config.wsgi
