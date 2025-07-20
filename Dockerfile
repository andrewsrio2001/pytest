# Use official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the FastAPI port
EXPOSE 8042

# Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8042"]
