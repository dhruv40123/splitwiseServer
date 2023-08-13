echo "BUILD START"

# Create a virtual environment
# python3.9 -m venv venv

# Activate the virtual environment (on Windows)
# source venv/Scripts/activate  # Use backslashes on Windows

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic

# Deactivate the virtual environment
deactivate  # Deactivate the virtual environment

echo "BUILD END"
