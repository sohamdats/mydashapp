#FROM ubuntu:latest

#RUN apt-get update

#RUN apt-get install -y software-properties-common vim

#RUN add-apt-repository ppa:jonathonf/python-3.6

#RUN apt-get update

#RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

#RUN python3.6 -m pip install pip --upgrade

#RUN python3.6 -m pip install wheel
FROM python:3.6
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt
RUN pip install plotly --upgrade



