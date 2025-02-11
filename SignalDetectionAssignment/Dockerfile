# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (to utilize Docker caching)
COPY requirements.txt .

# Install necessary Python packages
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Default command to run when the container starts
CMD ["python", "test_signal_detection.py"]
