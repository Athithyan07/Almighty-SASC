from django.core.management.base import BaseCommand
from core.models import ChatMessage

class Command(BaseCommand):
    help = 'Deletes all chat messages from the database.'

    def handle(self, *args, **options):
        ChatMessage.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all chat messages.'))