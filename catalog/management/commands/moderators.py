from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "create Group permission with 'delete_product' 'can_unpublish_product' "

    def handle(self, *args, **options):
        moderators, created = Group.objects.get_or_create(name="moderators")
        if created:
            self.stdout.write(self.style.SUCCESS("Группа создана"))
        else:
            self.stdout.write(self.style.SUCCESS("Группа уже создана"))

        try:
            delete_product = Permission.objects.get(codename="delete_product")
            can_unpublish_product = Permission.objects.get(
                codename="can_unpublish_product"
            )
        except ObjectDoesNotExist as e:
            self.stdout.write(self.style.ERROR(f"Не найдено право: {e}"))
            self.stdout.write(
                self.style.WARNING(f"Убедитесь что миграции применены: {e}")
            )
            return

        moderators.permissions.add(delete_product, can_unpublish_product)
        moderators.save()
        self.stdout.write(
            self.style.SUCCESS("Группа с правами модератора успешно создана")
        )
