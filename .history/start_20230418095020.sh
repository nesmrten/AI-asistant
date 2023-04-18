#!/bin/bash

# Create and activate the virtual environment
python -m venv venv
source venv/Scripts/activate

# Install required packages
pip install wheel
pip install -r requirements.txt

# Build the Cython extensions
python setup.py build_ext --inplace

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# Start the Flask app
flask run
