# Use an official Python base image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Copy everything from your local folder into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 (Flask default)
EXPOSE 5000

# Command to run your app
CMD ["python", "app.py"]
