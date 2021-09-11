from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self) -> str:
        return self.name
