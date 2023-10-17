FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
#EXPOSE 8000
#CMD python manage.py runserver