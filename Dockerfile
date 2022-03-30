FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock


RUN pip install pipenv

COPY src /src
WORKDIR /src
RUN pipenv install --dev --system --skip-lock

ENV PYTHONPATH "."

RUN scrapy crawl fotocasa_flats

