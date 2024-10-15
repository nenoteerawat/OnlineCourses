# Setup environment
## linux
```bash
export SECRET_KEY=secret
```

## windowns
```
set SECRET_KEY=secret
```

## install require lib
```bash
cd courseproject
pip install django
pip install -r requirements.txt
pip install django-crispy-forms
pip install crispy-bootstrap5
python manage.py makemigrations courseapp
python manage.py migrate
python manage.py runserver
```
http://127.0.0.1:8000/ofv/