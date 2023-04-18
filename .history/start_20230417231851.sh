#!/bin/bash

# Start the virtual environment
source ../../venv/Scripts/activate
# Set environment variables
export FLASK_APP=main.py
export FLASK_ENV=development

# Install required packages
pip install -r requirements.txt

# Start the Flask app
flask run
