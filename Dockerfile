# syntax=docker/dockerfile:1
FROM python:3.10-slim

# Prevent Python from writing pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY app/ .

# Expose the server port (Flask-SocketIO is configured to run on 5000)
EXPOSE 5000

# Command to start the server
CMD ["python", "main.py"]