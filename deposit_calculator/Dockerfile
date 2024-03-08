# установка python 3.11 с официального докерхаба
FROM python:3.11.0-alpine
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py"]
