FROM python:alpine3.8

ENV FLASK_APP "home_automation.py"

WORKDIR /

COPY requirements.txt requirements.txt
COPY / /

RUN apk add --update curl gcc g++ \
  && rm -rf /var/cache/apk/* \
  && pip install --upgrade pip \
  && pip install setuptools --upgrade

RUN pip install -r requirements.txt
RUN flask db init
RUN flask db migrate
RUN flask db upgrade
CMD flask run --host=0.0.0.0
