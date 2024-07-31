FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /app/app


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]