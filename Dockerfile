#FROM python:3.13
#
#ENV PYTHONDOVRWITEBYTECODE=1
#ENV PYTHONUNBUFERED=1
#WORKDIR /var/www/auto
#
#COPY requirements.txt .
#
#RUN pip install -r requirements.txt
#
#COPY . .
#
#COPY COPY ./wait-db.sh /wait-db.sh
#
#RUN apt-get update && apt-get install -y netcat-openbsd
#
#RUN chmod +x /wait-db.sh
#
#EXPOSE 8000
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/www/auto

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY ./wait-db.sh /wait-db.sh

RUN chmod +x /wait-db.sh

RUN apt-get update && apt-get install -y netcat-openbsd

EXPOSE 8000
