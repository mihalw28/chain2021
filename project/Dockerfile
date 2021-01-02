FROM python:3.9.0-slim-buster

WORKDIR /usr/src/app
COPY ./pyproject.toml ./poetry.lock ./

ENV PYTHONDONTWRITEBYTHECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

RUN pip install -U pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

# COPY ./entrypoint.sh .
# RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]