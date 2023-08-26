#!/bin/bash

# Create and activate a virtual environment
python3.9 -m venv venv
source venv/bin/activate

# Install requirements and collect static files
echo "BUILD START"
pip install -r requirements.txt
python manage.py collectstatic --clear
echo "BUILD END"

# Deactivate the virtual environment
deactivate
