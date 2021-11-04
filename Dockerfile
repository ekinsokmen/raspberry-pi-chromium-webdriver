FROM python:3.10-buster

RUN apt-get -y update
RUN apt-get install -y chromium chromium-driver

RUN pip install --upgrade pip
RUN pip install cryptography==3.3.2
RUN pip install selenium==4.0.0
