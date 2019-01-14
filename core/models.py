from django.conf import settings
from django.db import models
from redis import Redis

DEFAULT_MAX_LENGTH = 255


class City(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)


class Advert(models.Model):
    VIEWS_SET_KEY = 'advert_{}_set'

    title = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    description = models.TextField()
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    views_count = models.PositiveIntegerField(default=0)

    def get_views_key(self):
        return self.VIEWS_SET_KEY.format(self.id)

    def update_view_count(self):
        r = Redis(settings.REDIS_HOST, settings.REDIS_PORT)
        self.views_count = r.scard(self.get_views_key())
