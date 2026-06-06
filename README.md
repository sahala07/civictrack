# HEATBOX PORTAL

This is a Django 6.0 project configured for production deployment.

## Deployment preparation

1. Create a Python virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Set environment variables before starting the app:
   - `DJANGO_SECRET_KEY` : secret key for production
   - `DJANGO_DEBUG` : `False` in production
   - `DJANGO_ALLOWED_HOSTS` : comma-separated hostnames, e.g. `example.com,www.example.com`
   - `DJANGO_CSRF_TRUSTED_ORIGINS` : optional comma-separated HTTPS origins, e.g. `https://example.com`

3. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the application with Gunicorn:
   ```bash
   gunicorn civictrack_project.wsgi --bind 0.0.0.0:8000
   ```

## Docker deployment

Build the Docker image:
```bash
docker build -t heatbox-portal .
```

Run the app with Docker Compose:
```bash
docker compose up --build
```

Open `http://localhost:8000` in your browser.

To override the secret key, set an environment variable in `docker-compose.yml` or with a `.env` file.

## Deploying on Render

Render can deploy this app directly from your GitHub repository.

1. Create a new service on Render and choose "Web Service".
2. Connect your GitHub repo.
3. Set the environment to `Docker` and use the existing `Dockerfile`.
4. Add these environment variables in Render:
   - `DJANGO_SECRET_KEY` : a secret production key
   - `DJANGO_DEBUG` : `False`
   - `DJANGO_ALLOWED_HOSTS` : your domain(s), e.g. `yourdomain.com,www.yourdomain.com`
   - optional `DATABASE_URL` : Render Postgres connection string if you want a managed database
5. Deploy.

### Render database note

- If `DATABASE_URL` is not set, the app will use SQLite.
- For a production website, use Render Postgres so your data is persistent across deploys.

## Recommended hosting

- Render
- Railway
- DigitalOcean App Platform
- AWS Elastic Beanstalk
- Azure App Service

## Notes

- `DEBUG` is now controlled by `DJANGO_DEBUG`.
- `SECRET_KEY` is loaded from `DJANGO_SECRET_KEY`.
- `ALLOWED_HOSTS` is loaded from `DJANGO_ALLOWED_HOSTS`.
- Static files are served using `WhiteNoise`.
