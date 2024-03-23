# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Define environment variable to inform Python not to generate .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Define environment variable to ensure Python output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED 1

# Run server.py when the container launches
CMD ["python", "app.py"]
