from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User

class Command(BaseCommand):

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        # For each user
        for user in User.objects.all():
            # If that user is not a superuser ie. @admin, delete
            if(user.is_superuser == False):
                user.delete()
