from django.db import IntegrityError
from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            user = CustomUser.objects.create(
                username="admin",
                email="admin@example.com",
                is_superuser=True,
                is_staff=True,
            )
            user.set_password("admin123")
            user.save()
            self.stdout.write(self.style.SUCCSES("Пользователь успешно создан"))
        except IntegrityError as e:
            self.stdout.write(self.style.WARNING("Пользователь уже создан"))
