FROM python:3.10.20-alpine3.22

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]