from django.conf import settings
from django.views.generic import ListView, DetailView
from redis import Redis

from core.models import Advert


class AdvertsView(ListView):
    model = Advert
    queryset = Advert.objects.select_related('user', 'city').order_by('-id')
    context_object_name = 'adverts'
    template_name = 'core/adverts.html'


class AdvertDetailView(DetailView):
    model = Advert
    queryset = Advert.objects.select_related('user', 'city')
    context_object_name = 'advert'
    template_name = 'core/advert.html'

    def get_object(self, queryset=None):
        advert = super().get_object(queryset)
        r = Redis(settings.REDIS_HOST, settings.REDIS_PORT)
        if self.request.user.is_authenticated:
            r.sadd(advert.get_views_key(), f'user:{self.request.user.id}')
        else:
            r.sadd(advert.get_views_key(), f'ip:{self.request.META["REMOTE_ADDR"]}')

        return advert
