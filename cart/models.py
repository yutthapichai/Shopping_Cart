from django.db import models
from shop.models import Product

class Card(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = ('Cart',)
        ordering = 'Date_added'
    def __str__(self):
        return self.cart_id
# Create your models here.
