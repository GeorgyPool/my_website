from django.db import models


class Category(models.Model):
    name_category = models.CharField(
        max_length=200,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    descriptions = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name_product = models.CharField(
        max_length=200,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    descriptions = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите текст описания продукта",
    )
    image = models.ImageField(
        upload_to="product/",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Добавьте фото продукта",
    )
    category = models.ForeignKey(
        to=Category, on_delete=models.SET_NULL, related_name="products", null=True
    )
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Название продукта: {self.name_product}, цена за покупку: {self.purchase_price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["purchase_price", "name_product"]
