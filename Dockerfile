FROM python:3
LABEL maintainer="Daniel <d.miralles-vargas@mycit.com>"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD FLASK_APP=piton.py flask run
