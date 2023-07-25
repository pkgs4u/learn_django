
from django.utils import timezone
from django.db import models

import products.models


# Create your models here.
class Product(models.Model):
    item_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='item_ID')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2500)

class OrderedItems(models.Model):
    ordID = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='order_ID')
    ord_item = models.ForeignKey(Product, to_field='item_id', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ord_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.quantity} of {self.ord_item.name}"
    def get_total_item_price(self):
        return self.quantity * self.ord_item.price