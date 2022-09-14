from celery import shared_task
from django.core.mail import send_mail as django_send_mail


@shared_task
def send_mail_to_admin(text, email):
    django_send_mail("Notification", text, email, ['admin@example.com'])


@shared_task
def send_mail_to_owner(text, email):
    django_send_mail("Notification", text, 'admin@example.com', [email])
