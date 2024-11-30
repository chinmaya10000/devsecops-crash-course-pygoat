# Use a stable Python base image
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Install dependencies for psycopg2 and other system utilities
RUN apt-get update && apt-get install --no-install-recommends -y \
    dnsutils libpq-dev python3-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables to improve Python behavior
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip and install Python dependencies
RUN python -m pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose the port used by the application
EXPOSE 8000

# Run database migrations and start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "6", "pygoat.wsgi"]
