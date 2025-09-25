# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy requirements and install
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]