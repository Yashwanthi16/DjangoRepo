# Set default values for Django superuser
FROM python:3
RUN pip install django==3.2
COPY . .
RUN python -m pip install Pillow
RUN python manage.py migrate
CMD ["python","manage.py", "runserver","0.0.0.0:8002"]

