from django.db import models


class Spare(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.CharField(max_length=50)

    def __str__(self):
        return self.name
