#MOTORIEC - STANDALONE DJANGO PROJECT

This is a complete local-development project, not just a set of replacement files.
It includes manage.py, Django settings, URL configuration, the djangoapp application,
HTML templates, CSS, JavaScript, and the Spare model.

RUN ON WINDOWS POWERSHELL

1. Open PowerShell in this folder (the folder containing manage.py).
2. Create a virtual environment (recommended):
   py -m venv .venv
3. Activate it:
   .\.venv\Scripts\Activate.ps1
4. Install Django:
   python -m pip install -r requirements.txt
5. Create the database tables:
   python manage.py migrate
6. Start the website:
   python manage.py runserver
7. Open http://127.0.0.1:8000/register/ to create the first user.

IMPORTANT NOTES

- The project creates its own db.sqlite3 the first time you run migrate.
- It does not include your old project's db.sqlite3. To bring across old spare inventory
  records, copy the old db.sqlite3 into this project root BEFORE running migrate, or
  export/import the records separately. Keep a backup first.
- Password-reset emails are printed in the terminal running runserver. This is for local
  testing; it does not send real emails.
- Copy helmet1.jpg, helmet2.jpg, and helmet3.jpg into djangoapp/static/images/ if you
  want the three helmet photos to appear on the homepage.
- DEBUG=True and the development SECRET_KEY are for local practice only, not production.
