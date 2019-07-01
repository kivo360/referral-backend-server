FROM python:3.7

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install sanic
RUN pip install sanic_cors
RUN pip install sanic_limiter

ENV SQLDATABASE=postgresql://funbags64:babelcrack@funguana-closed-beta.c8wkqxjlpy8o.us-east-1.rds.amazonaws.com:5432/closedbeta
ENV SQLTEMP=sqlite:///temp.db
ENV REDISHOST=localhost
ENV REDISPORT=6379
ENV MAILGUNPASSWORD=55ac07a03d1e3d61b7de4d379a118cfe
ENV MAILGUNAPI=key-b42d805f39588a464b8db0daaeb0d380
ENV STRIPEKEY=sk_live_WxCFh6xG9z079NoOOy4Nufbp


RUN python setup.py install

EXPOSE 9000

CMD ["python", "referral/app.py"]