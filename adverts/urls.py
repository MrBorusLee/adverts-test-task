from django.contrib import admin
from django.urls import path

from core.views import AdvertsView, AdvertDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AdvertsView.as_view(), name='adverts'),
    path('advert/<int:pk>/', AdvertDetailView.as_view(), name='advert')
]
