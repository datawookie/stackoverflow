FROM python:3.10

ARG CONTAINER_HOME=/var/www

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

RUN pip3 install -r requirements.txt
