from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField("Ім'я", max_length=24)
    user_email = models.EmailField("Пошта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

