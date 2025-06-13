from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from data.models import Profile

class Command(BaseCommand):
    help = "Seed the database with a superuser"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        if not User.objects.filter(email="superuser@gmail.com").exists():
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

        
        if not User.objects.filter(email="admin@gmail.com").exists():
            user = User(
                username="Admin 1",
                email="admin@gmail.com",
                is_staff=True,
                is_superuser=True,
                role='admin'
            )
            user.set_password("admin321")
            user.save()

            self.stdout.write(self.style.SUCCESS("Superuser created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists."))

        
        profile_data = [
            {"key": "Alamat", "value": "Telaga Sari, Balikpapan Kota", "type": "inti"},
            {"key": "Nama Ketua RT", "value": "Gandung Kriswanto", "type": "inti"},
            {"key": "Kegiatan Rutin", "value": "Kerja Bakti setiap hari sabtu", "type": "tambahan"},
        ]

        for item in profile_data:
            obj, created = Profile.objects.get_or_create(
                key=item["key"],
                defaults={
                    "value": item["value"],
                    "type": item["type"],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Profile '{item['key']}' created."))
            else:
                self.stdout.write(self.style.WARNING(f"Profile '{item['key']}' already exists."))