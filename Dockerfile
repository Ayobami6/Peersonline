FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

# Install the Python dependencies from requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir gunicorn

COPY . .

# Start the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "peers.wsgi:application"]
