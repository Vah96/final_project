from tags.models import Tag
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete all tags'

    def handle(self, *args, **kwargs):
        Tag.objects.all().delete()
