python-tutorial
===============

Repo for learning python and django

Print version of django (if installed)
```python -c "import django; print(django.get_version())"```

### 1. Setup

Create new django-project
```django-admin.py startproject notes_project```

Run server
```python manage.py runserver```

Sync database (first time create user)
```python manage.py syncdb```

Create new app
```python manage.py startapp notes```

### 2. Create Models

Create model in  notes/models.py

```
Note

- user
- date
- text
```

Output the statement to create model-tables
```python manage.py sql notes```

To run the commands and create models use
```python manage.py syncdb```

With the interactive shell you can test your models
```python manage.py shell```

For example fetch all notes use
```Note.objects.all()```

### 3. Use admin panel

You can enter the admin panel with the user-pw combination which was set first
```http://localhost:8000/admin```

There you can create groups, users and objects of the model (Notes)

### 4. Create views

- Write a action in notes/views.py
- Create notes/urls.py to add URL configs
- Create a pattern which calls  the action if it matches on the url
- Add notes-url to notes_project/urls.py
