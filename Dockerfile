FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV=production

COPY . .

EXPOSE 8084

CMD ["gunicorn", "--preload", "-w", "4", "-b", "0.0.0.0:8084", "app:create_app()"]
