
echo "BUID START"
python -m venv venv
./venv\Scripts\activate
python -m pip install -r requirements.txt
echo "BUID END" 
python manage.py runserver 
