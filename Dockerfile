FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /blog_project_api

WORKDIR /blog_project_api

ADD . /blog_project_api/

RUN pip install pipenv
RUN pipenv install

