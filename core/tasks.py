import logging

from adverts.celery import app
from core.models import Advert

logger = logging.getLogger(__name__)


@app.task
def update_views_count():
    for advert in Advert.objects.all():
        old_views_count = advert.views_count
        advert.update_view_count()
        if old_views_count != advert.views_count:
            advert.save()
            logger.info(f'set views count for advert #{advert.id}')
