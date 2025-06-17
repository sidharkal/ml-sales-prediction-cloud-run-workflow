FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --xtno-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
