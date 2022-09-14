import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
app = Celery('store')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'store_update': {
        'task': 'catalog.tasks.store_update',
        'schedule': crontab(minute='*/30'),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
