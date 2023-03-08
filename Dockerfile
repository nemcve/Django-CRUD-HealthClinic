FROM python:3.9.16-slim-buster
WORKDIR /djangoapp
COPY ./HealthClinic/ ./
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /djangoapp/requirements.txt --no-cache-dir
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
