FROM ubuntu:latest
#FROM python:latest

RUN apt install rabbitmq-server -y 

ADD ./start.sh ./
RUN chmod +x ./start.sh 

CMD ['./start.sh']


EXPOSE 5672
