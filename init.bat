REM use this to set up actual program
pip install -r requirements.txt
cd FFR
manage.py makemigrations
manage.py migrate
manage.py runserver