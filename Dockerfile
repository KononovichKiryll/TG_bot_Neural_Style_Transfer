FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

ENV TG_BOT_TOKEN 1

CMD ["python", "app.py"]
