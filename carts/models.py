from django.db import models

from shop.models import User
from shop.models import Product


class Cart(models.Model):
    Cart_id = models.AutoField(primary_key=True)
    Customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Product_title = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_per_qty = models.DecimalField(max_digits=10, decimal_places=2)
    total_ammount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.Product_title)

    
    class Meta:
        verbose_name_plural = "Carts"