from aphorisms.models import Aphorism
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete all aphorisms'

    def handle(self, *args, **kwargs):
        Aphorism.objects.all().delete()
