# Use Python 3.11 slim image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Use the Azure port
ENV PORT=8080

# Expose port (Azure needs this)
EXPOSE 8080

# Run the app with Gunicorn + Uvicorn workers
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app:app", "--bind", "0.0.0.0:8080"]
