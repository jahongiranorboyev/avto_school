FROM python:3.13

WORKDIR /var/www/avto

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000