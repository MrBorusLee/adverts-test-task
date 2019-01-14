import factory

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .models import Advert, City


class CityFactory(factory.DjangoModelFactory):
    name = 'City'

    class Meta:
        model = City


class UserFactory(factory.DjangoModelFactory):
    username = factory.Faker('email')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = make_password('password')
    is_superuser = True

    class Meta:
        model = User


class AdvertFactory(factory.DjangoModelFactory):
    title = factory.Faker('text', max_nb_chars=40)
    description = factory.Faker('text', max_nb_chars=500)
    city = factory.SubFactory(CityFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Advert
