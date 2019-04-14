# AppSpeedXrayWebsite

## Usage
1. Create super user
```bash
python3 manage.py migrate
python3 manage.py createsuperuser --email admin@example.com --username admin
```
2. Create Xray app
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

