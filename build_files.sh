

# Install requirements and collect static files
echo "BUILD START"
pip install -r requirements.txt
python3.9 manage.py collectstatic --clear
echo "BUILD END"

