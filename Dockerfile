FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

# Initialize and update submodules
RUN git init && git config user.email "build@render.com" && git config user.name "Build" && git add . && git submodule update --init --recursive 2>/dev/null || true

EXPOSE 8000

CMD ["gunicorn", "civictrack_project.wsgi", "--bind", "0.0.0.0:8000", "--log-file", "-"]
