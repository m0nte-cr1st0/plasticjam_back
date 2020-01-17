import json

from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    help = 'Adds users from json file.'

    def handle(self, *args, **options):
        with open('users.json') as f:
            data_list = json.load(f)
        User.objects.bulk_create([User(**q) for q in data_list])
