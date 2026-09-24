from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


def validation_number(phone_number: str):
    if phone_number and not phone_number.isdigit():
        raise ValidationError("Номер должен состоять только из цифр")
    return phone_number


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона",
        blank=True,
        null=True,
        validators=[validation_number],
    )
    country = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Страна"
    )
    avatar = models.ImageField(upload_to="users/avatar/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("password1",)

    def __str__(self):
        return self.email
