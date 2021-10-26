from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def __init__(self):
        super().__init__()

    def handle(self. *args, **options):
        # Get all users
        User = get_user_model()
        users = User.objects.all()
        # For each user
        for user in users:
            # If that user is not a superuser ie. @admin, delete
            if(user.is_superuser == False):
                user.delete()
