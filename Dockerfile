FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=civictrack_project.settings
ENV DJANGO_SECRET_KEY=build-time-secret
ENV DJANGO_DEBUG=False

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

RUN python manage.py collectstatic --noinput --clear

EXPOSE 8000

CMD ["gunicorn", "civictrack_project.wsgi", "--bind", "0.0.0.0:8000", "--log-file", "-"]
