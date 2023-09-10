FROM python:3.11-slim-buster
WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .
COPY app ./app

CMD ["python3", "app/main.py"]