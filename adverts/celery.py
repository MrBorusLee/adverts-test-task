import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adverts.settings')

app = Celery('adverts')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sync-views': {
        'task': 'core.tasks.update_views_count',
        'schedule': timedelta(seconds=30)
    },
}
