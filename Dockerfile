FROM python:3.8

RUN apt-get -y update
RUN apt-get install -y chromium chromium-driver

RUN pip install --upgrade pip
RUN pip install selenium
