from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, related_name='products')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    total_price = models.IntegerField(verbose_name='Сумма заказа', default=0)
    add_datetime = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)


