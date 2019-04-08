FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:5000 wsgi