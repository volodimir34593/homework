from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    new = models.BooleanField(default=False)  # Додали новий атрибут

    def __str__(self):
        return self.name
# Create your models here.
