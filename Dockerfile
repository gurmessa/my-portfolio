# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if any, e.g., gcc for psycopg2 or other packages)
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

#  entrypoint.sh make it executable
RUN chmod +x /app/entrypoint.sh

# Use the entrypoint script to run migrations before starting the server
ENTRYPOINT ["/app/entrypoint.sh"]




CMD ["gunicorn", "--bind", "0.0.0.0:8081", "myportfolio.wsgi:application"]


