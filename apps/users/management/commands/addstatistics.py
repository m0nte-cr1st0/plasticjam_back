import json

from django.core.management.base import BaseCommand

from apps.users.models import Statistic


class Command(BaseCommand):
    help = 'Adds users from json file.'

    def handle(self, *args, **options):
        with open('users_statistic.json') as f:
            data_list = json.load(f)
        Statistic.objects.bulk_create([Statistic(**q) for q in data_list])
