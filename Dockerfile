# Use official TensorFlow CPU image
FROM tensorflow/tensorflow:2.13.0-py3

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install Flask
RUN pip install --no-cache-dir Flask==2.3.2 numpy==1.25.2

# Expose port 10000
EXPOSE 10000

# Start the Flask app
CMD ["python", "app.py"]