FROM python:3.8

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app
ENV PYTHONPATH /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python3 app/create_db.py && \
    uvicorn --host=0.0.0.0 app.main:app
