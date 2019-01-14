from django.contrib import admin

from core.models import Advert, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    pass
