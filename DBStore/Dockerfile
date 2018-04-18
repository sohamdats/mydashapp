FROM ubuntu:latest

RUN apt-get update && apt-get install -y cron

RUN apt-get install -y software-properties-common vim

RUN add-apt-repository ppa:jonathonf/python-3.6

RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

RUN python3.6 -m pip install pip --upgrade

RUN python3.6 -m pip install wheel

WORKDIR /dbstore

ADD . /dbstore

RUN pip install -r requirements.txt

#ADD crontab /etc/cron.d/dbstore-cron

#RUN chmod 0644 /etc/cron.d/dbstore-cron


