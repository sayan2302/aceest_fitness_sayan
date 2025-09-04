# Use an official lightweight Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Flask port
EXPOSE 5173

# Run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5173"]

