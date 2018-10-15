FROM python:3.5

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8096
EXPOSE 80

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver"]