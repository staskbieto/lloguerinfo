FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv
RUN pipenv install --dev --system --skip-lock

COPY smartlibrary_operations /smartlibrary_operations
COPY assets /assets

WORKDIR /

EXPOSE 8000
ENV PYTHONPATH "."

ENTRYPOINT ["python", "smartlibrary_operations/run.py"]

