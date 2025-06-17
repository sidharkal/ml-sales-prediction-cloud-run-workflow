# Use a minimal Python 3.10 base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the training script first to generate model.pkl
RUN python train_model.py

# Expose port for Flask
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
