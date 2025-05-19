from django.db import models
from django.urls import reverse

class Hobby(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to='hobbies/')
    slug = models.SlugField("URL", unique=True)
    internal_url = models.CharField(
        "Внутренний URL",
        max_length=100,
        help_text="Например: /snowboarding/",
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        if self.internal_url:
            return self.internal_url
        return reverse('hobby_detail', args=[str(self.slug)])

    def __str__(self):
        return self.name