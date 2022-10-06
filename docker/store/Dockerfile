FROM python:3.8

COPY ./store/requirements.txt /

RUN pip install -r requirements.txt

COPY ./docker/store/docker-entrypoint.sh ./docker/store/wait-for-command.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh

COPY ./store/ /app

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/runserver.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]