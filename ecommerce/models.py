from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, default="No description available")
    price = models.FloatField()
    image = models.ImageField()

    # Rinomina gli item sul db.
    def __str__(self):
        return self.name


