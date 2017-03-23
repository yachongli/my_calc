FROM centos:7
#FROM python:latest

#ADD sources.list /etc/yum.
RUN yum update -y
RUN yum install epel-release -y
RUN yum update -y
RUN yum install python-pip openssl-devel -y 

RUN mkdir /root/.pip
ADD pip.conf /root/.pip/

WORKDIR /etc/apt

RUN pip install --upgrade pip


RUN mkdir /req
ADD requirements.txt /req 
WORKDIR /req 
RUN pip install -r requirements.txt


RUN yum clean all 
WORKDIR ~/.cache
RUN rm -rf pip 


WORKDIR /

#EXPOSE 8080
