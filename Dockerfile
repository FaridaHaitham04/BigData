# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app/pipeline/

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Start interactive bash shell
CMD ["bash"]