# Usa l'immagine ufficiale di Python
FROM python:3.11-slim

# Imposta le variabili di ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Imposta la directory di lavoro
WORKDIR /app

# Installa le dipendenze di sistema necessarie per psycopg2-binary
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && apt-get clean

# Installa le dipendenze Python
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --default-timeout=100 -r requirements.txt

# Copia il progetto
COPY . /app/

# Espone la porta 8000 per Django
EXPOSE 8000

# Esegui il server Django
CMD ["gunicorn", "projectBE.wsgi:application", "--bind", "0.0.0.0:8000"]
