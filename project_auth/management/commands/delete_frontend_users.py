from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete all frontend user. It will be removed all relation aphorisms with user too'

    def handle(self, *args, **kwargs):
        User.objects.filter(is_superuser=0).delete()
