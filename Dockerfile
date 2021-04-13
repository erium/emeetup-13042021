FROM python:3.8-slim-buster
WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip3 install Flask flask-swagger flask-swagger-ui
COPY . .

CMD ["flask", "run"]
EXPOSE 5000