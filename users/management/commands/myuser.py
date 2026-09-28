from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            username="admin",
            email="admin@example.com",
            is_superuser=True,
            is_staff=True,
        )
        user.set_password("admin123")
        user.save()
        print("created superuser")
