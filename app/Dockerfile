# syntax=docker/dockerfile:1
FROM python:3.10-slim

# Working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the server port
EXPOSE 8080

# Command to start the server
CMD ["waitress-serve", "--host=0.0.0.0", "--call", "main:create_app"]