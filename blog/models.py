from django.db import models


class BlogPaper(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    text = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog_paper/", blank=True, null=True, help_text="Фото для превью"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["created_at", "updated_at"]
