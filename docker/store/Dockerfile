FROM python:3.8

COPY ./store/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./store/ /app

COPY ./docker/store/runserver.sh /

RUN chmod +x /runserver.sh

EXPOSE 8000

CMD ["/runserver.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]