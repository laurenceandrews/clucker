from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User
from faker import Faker


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        # Do it 100 times
        for i in range(100):
            # Create randomised user using Faker
            self.user = User.objects.create_user(
                username = "@" + self.faker.unique.user_name(),
                first_name = self.faker.first_name(),
                last_name = self.faker.last_name(),
                email = self.faker.unique.email(),
                password = self.faker.password(),
                bio = self.faker.text()
                )
            # Save the user
            User.save(self.user)
