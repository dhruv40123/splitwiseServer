echo "BUILD START"

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (on Windows)
source venv/Scripts/activate  # Use backslashes on Windows

# Install dependencies
python -m pip install -r requirements.txt

# Collect static files
python manage.py collectstatic

# Deactivate the virtual environment
deactivate  # Deactivate the virtual environment

echo "BUILD END"
