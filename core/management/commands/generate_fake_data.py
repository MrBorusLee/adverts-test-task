from django.core.management import BaseCommand

from core.fixtures import AdvertFactory


class Command(BaseCommand):

    def handle(self, *args, **options):
        AdvertFactory.create_batch(30)
        self.stdout.write(self.style.SUCCESS('Successfully created 30 fake adverts'))
