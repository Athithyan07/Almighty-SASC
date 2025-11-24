from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates 5 teacher users with simple passwords.'

    def handle(self, *args, **options):
        User = get_user_model()
        for i in range(1, 6):
            username = f'teacher{i}'
            email = f'teacher{i}@example.com'
            password = 'password123'
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f'Successfully created teacher user: {username}'))
            else:
                self.stdout.write(self.style.WARNING(f'Teacher user {username} already exists.'))