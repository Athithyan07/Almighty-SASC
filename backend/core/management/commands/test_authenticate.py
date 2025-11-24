from django.core.management.base import BaseCommand
from django.contrib.auth import authenticate
from core.models import User

class Command(BaseCommand):
    help = 'Tests the Django authenticate function with provided credentials.'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username to test')
        parser.add_argument('password', type=str, help='The password to test')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']

        self.stdout.write(self.style.SUCCESS(f"Attempting to authenticate user '{username}' with password '{password}'..."))

        user = authenticate(username=username, password=password)

        if user is not None:
            self.stdout.write(self.style.SUCCESS(f"Authentication successful for user: {user.username} (ID: {user.id})"))
            self.stdout.write(self.style.SUCCESS(f"Is superuser: {user.is_superuser}"))
            self.stdout.write(self.style.SUCCESS(f"Is active: {user.is_active}"))
        else:
            self.stdout.write(self.style.ERROR("Authentication failed."))