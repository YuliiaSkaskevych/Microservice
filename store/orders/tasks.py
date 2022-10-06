import requests, json
from celery import shared_task
from django.core.mail import send_mail as django_send_mail
from orders.models import Order


@shared_task
def send_mail_to_admin(text, email):
    django_send_mail("Notification", text, email, ['admin@example.com'])

@shared_task
def send_mail_to_owner(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order # {}'.format(order_id)
    message = f'Dear {order.owner}Your order {order.pk} was created successfully!'
    mail_sent = django_send_mail(subject,
                                 message,
                                 'admin@example.com',
                                 [order.email])
    return mail_sent


@shared_task
def send_to_api(title):
    data = {"title": title}
    data_json = json.dumps(data)
    print(data_json)
    requests.post('http://warehouse:8000/orders/', data_json)
