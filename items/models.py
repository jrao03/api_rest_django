from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0, validators=[MinValueValidator(0)])
    department = models.CharField(max_length=20)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)], default=0)