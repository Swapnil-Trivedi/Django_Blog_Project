FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /BLOG

ADD . /BLOG

RUN pip install -r requirements.txt

COPY . /BLOG

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
