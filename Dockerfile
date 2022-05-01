FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN apt-get install -y cron

WORKDIR /

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv

COPY lloguerinfo /lloguerinfo
WORKDIR /lloguerinfo
RUN pipenv install --dev --system --skip-lock

ENV PYTHONPATH "."
EXPOSE 8000
EXPOSE 6800

RUN crontab

RUN python manage.py crontab add

CMD  service cron start & scrapyd & python manage.py runserver 0.0.0.0:8000

