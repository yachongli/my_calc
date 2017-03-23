FROM ubuntu:latest
#FROM python:latest

ADD sources.list /etc/apt
RUN apt update -y
RUN apt install python python-pip libmysqlclient-dev  libssl-dev -y




RUN mkdir /root/.pip
ADD pip.conf /root/.pip/

WORKDIR /etc/apt

RUN pip install --upgrade pip


RUN mkdir /req
ADD requirements.txt /req 
WORKDIR /req 
RUN pip install -r requirements.txt

RUN apt install rabbitmq-server -y 

RUN apt clean all 
WORKDIR ~/.cache
RUN rm -rf pip 


WORKDIR /

#EXPOSE 8080
