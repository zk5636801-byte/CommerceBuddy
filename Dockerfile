FROM python:3.12-slim

WORKDIR /app

# Copy application files
COPY . .

# Set environment defaults
ENV PORT=8000
EXPOSE 8000

# Start CommerceBuddy
CMD ["python", "backend/app.py"]
