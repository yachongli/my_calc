#FROM horizon:latest
FROM ubuntu:latest

ADD sources.list /etc/apt
RUN apt update -y
RUN apt install python python-pip libmysqlclient-dev  libssl-dev -y
#RUN service rabbitmq-server start

#RUN apt install apache2 libapache2-mod-wsgi -y 

RUN mkdir /root/.pip
ADD pip.conf /root/.pip/

RUN ls -al ~/.pip 

WORKDIR /etc/apt

#RUN pip install --upgrade pip

#RUN service rabbitmq-server start
#RUN rabbitmqctl add_user nca47 nca47 
#RUN rabbitmqctl set_permissions openstack ".*" ".*" ".*"

RUN mkdir /req
ADD requirements.txt /req 
WORKDIR /req 
RUN pip install -r requirements.txt

RUN apt clean all 
WORKDIR ~/.cache
RUN rm -rf pip 

EXPOSE 8001
