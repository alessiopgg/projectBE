from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, default="No description available")
    price = models.FloatField()
    image = models.ImageField()

    # Rinomina gli item sul db.
    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

