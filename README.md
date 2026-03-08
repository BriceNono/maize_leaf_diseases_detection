# Maize Leaf Disease Detection using CNN

This project is a deep learning web application that detects maize leaf diseases using a Convolutional Neural Network (CNN).

## Features

- Upload maize leaf image
- CNN model predicts disease
- Displays disease name and confidence
- Web interface built with Flask
- Deployable on Render

## Diseases Detected

- Healthy
- Corn Rust
- Northern Leaf Blight
- Gray Leaf Spot

## Run Locally

Install dependencies

pip install -r requirements.txt

Run application

python app.py

Open browser

http://127.0.0.1:5000

## Deployment

This project can be deployed on Render.

Start command:

gunicorn app:app# maize_leaf_diseases_detection
