# Use a smaller, production-friendly Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file first to use Docker's cache
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables for production
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Run the application with Gunicorn, which is more production-ready
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
