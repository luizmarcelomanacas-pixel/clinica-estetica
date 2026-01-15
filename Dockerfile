FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# 🔥 Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

ENV PORT=8080

CMD exec gunicorn sistema.wsgi:application --bind 0.0.0.0:$PORT
