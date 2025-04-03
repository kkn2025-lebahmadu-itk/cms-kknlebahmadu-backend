from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Seed the database with a superuser"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        if not User.objects.filter(email="admin@example.com").exists():
            user = User(
                username="Superuser",
                email="superuser@gmail.com",
                is_staff=True,
                is_superuser=True,
                role='superuser'
            )
            user.set_password("superuser1")
            user.save()

            self.stdout.write(self.style.SUCCESS("Superuser created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists."))