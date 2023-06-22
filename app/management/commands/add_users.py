from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'creates dummy users in the database'


    def handle(self, *args, **options):

        name = input("Name:\n>")
        email = input("Email:\n>")
        role = input("Role:\n>")

        
        User.objects.create(name=name, email=email, role=role, is_active=True)
        
        self.stdout.write(self.style.SUCCESS("Successfully added users"))