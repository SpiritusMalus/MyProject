from django.contrib.auth.models import AbstractUser
from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name="имя продукта", max_length=128)
    image = models.ImageField(upload_to="products_images", blank=True)
    description = models.TextField(verbose_name="описание продукта", blank=True)
    price = models.CharField(max_length=15, verbose_name="цена продукта", default=0)
    quantity = models.PositiveIntegerField(verbose_name="количество на складе", default=0)
    is_active = models.BooleanField(verbose_name="продукт активен", default=True, db_index=True)


class User(AbstractUser):
    pass
