import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for c in phones:
            phone = Phone(id=c['id'],
                          name=c['name'],
                          image=c['image'],
                          price=c['price'],
                          release_date=c['release_date'],
                          lte_exists=c['lte_exists'],
                          slug=c['name'])

            phone.save()
            pass
