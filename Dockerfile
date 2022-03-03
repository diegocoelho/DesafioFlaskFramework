FROM python:3.6
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt

EXPOSE 5000