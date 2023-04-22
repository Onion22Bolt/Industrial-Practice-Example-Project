FROM python:3.10

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:fastapi", "--host", "0.0.0.0", "--port", "7777"]