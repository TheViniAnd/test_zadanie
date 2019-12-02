#FROM python:3
#MAINTAINER test
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
#COPY . /app
#WORKDIR /app
#RUN pip install -r requirements.txt
#ENTRYPOINT ['python']
#CMD python3 /1/test1/manage.py runserver 0.0.0.0:8000
FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /test1
WORKDIR /test1
ADD requirements.txt /test1/
RUN pip install -r requirements.txt
ADD . /test1/