# PeopleDesk HRMS — Django + Vercel + Supabase

A Django Human Resource Management System starter with a dashboard, department overview, employee directory/search, employee CRUD, and Django Admin.

## Stack
- Django 5.2
- Django templates + CSS
- Supabase Postgres for persistent application data in production
- Supabase Storage private bucket for future HR document uploads
- Vercel Python/Django deployment
- SQLite fallback for local development only

## Local development (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py shell -c "from hrms.models import Department; [Department.objects.get_or_create(name=n) for n in ['Engineering','Finance','HR & Talent Operations','Other']]"
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/admin/ to sign in. The dashboard and employee pages are protected by Django login; use the admin login for the demonstration.

## Vercel deployment
Vercel supports Django applications and detects the root-level `manage.py`. Import this Git repository into Vercel and configure the environment variables below in Project Settings → Environment Variables.

Required:
- `DJANGO_SECRET_KEY`: a long random secret, not committed to Git.
- `DJANGO_DEBUG`: `false`
- `DJANGO_ALLOWED_HOSTS`: include the assigned Vercel host (hostnames only, comma-separated).
- `CSRF_TRUSTED_ORIGINS`: `https://*.vercel.app` plus any custom HTTPS domain you add.
- `DATABASE_URL`: Supabase Postgres connection string with SSL enabled (use the Supabase connection string suited for serverless deployments/pooler where appropriate).
- `SUPABASE_URL`: project API URL.
- `SUPABASE_SERVICE_ROLE_KEY`: server-side secret key only; never expose it in browser code.
- `SUPABASE_STORAGE_BUCKET`: `hrms-private-documents` (or the bucket name you create).

Deploy from the repository's `main` branch. Once environment variables are set, redeploy so the build/runtime receives them.

### Database setup
Run migrations against the production Supabase database:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py shell -c "from hrms.models import Department; [Department.objects.get_or_create(name=n) for n in ['Engineering','Finance','HR & Talent Operations','Other']]"
```
Do not use the tracked/local SQLite file as the production database. Vercel function filesystems are not a persistent database.

### Supabase Storage
Create a **private** bucket named `hrms-private-documents`. Private HR files should not be made public. The `hrms/storage.py` helper uploads through the Supabase Storage API from the server; no storage credentials belong in frontend code. The current starter does not yet present employee document upload fields, so the helper is the integration point for a future attachment field/workflow.

## Security notes
- Dashboard and employee views require Django login. Sign in at `/admin/login/` with a staff/superuser account.
- Use unique secrets in Vercel environment variables; never commit `.env`, service-role keys, database passwords, or production data.
- Keep employee data private. This starter is for demonstration and still needs production-grade role permissions, audit logging, backups, retention rules, and security testing before real HR data is entered.
