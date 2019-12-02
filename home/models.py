from django.db import models
from django.utils import timezone


class Mod(models.Model):
    title = models.CharField(verbose_name='Заголовок:', max_length=100)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title