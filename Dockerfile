FROM python:3.7.11-alpine3.14

WORKDIR /app

RUN apk add chromium chromium-chromedriver

RUN pip3 install selenium flask

COPY . .

EXPOSE 5000

CMD python3 app.py
