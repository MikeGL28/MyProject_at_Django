from django.db import models

class Certificate(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to='certificates/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title