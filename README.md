# PeopleDesk HRMS — Django starter

A starter Human Resource Management System for Engineering, Finance, and HR & Talent Operations.

## Requirements
- Python 3.10+
- VS Code (recommended)
- Internet is needed only to install Django

## Run on Windows in VS Code
1. Extract this ZIP.
2. In VS Code, choose **File → Open Folder** and select the `django_hrms_starter` folder.
3. Open **Terminal → New Terminal**.
4. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If `py` is not recognised, try `python` instead. If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`.

5. Install Django:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Create database tables and seed the four departments:

   ```powershell
   python manage.py makemigrations hrms
   python manage.py migrate
   python manage.py shell -c "from hrms.models import Department; [Department.objects.get_or_create(name=n) for n in ['Engineering','Finance','HR & Talent Operations','Other']]"
   ```

7. Create an admin login:

   ```powershell
   python manage.py createsuperuser
   ```

   Follow the prompts to set a username and password.

8. Start the site:

   ```powershell
   python manage.py runserver
   ```

9. Open http://127.0.0.1:8000/ in your browser.
10. Open http://127.0.0.1:8000/admin/ to add employees and manage departments.

## Included
- Dashboard with employee and department counts
- Department cards for the seeded departments
- Employee directory with search
- Django admin to add/update employees and departments
- SQLite database for local development

## Important
This is a learning/development starter, not a production-ready HR platform. Before production, add authentication and permissions for all pages, secure secrets, validation, audit logs, backups, tests, and privacy controls. Do not add real employee data until access controls are in place.
