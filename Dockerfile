FROM python:3.9-alpine3.13
LABEL maintainer="Armandres"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
COPY ./first_django_project /first_django_project

WORKDIR /first_django_project
EXPOSE 8080

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home first_django_project

ENV PATH="/py/bin:$PATH"