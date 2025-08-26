# Use Python as the base image
From python:3.11-slim

# Define the working directory where all subsequent commands will be run
WORKDIR /app

# Install required system packages/dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgthread-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the dependency file
COPY requirements.txt .

# Install Python dependecies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p data/raw_videos data/frame_actions data/keypoints data/normalized_samples \
    models/trained_models models/checkpoints models/vocabulary \
    logs/training_logs logs/api_logs \
    outputs/confusion_matrices outputs/predictions outputs/reports

# Expose port for the API (for later)
EXPOSE 8000

# Default command
CMD ["python", "src/capture/capture_samples.py"]

