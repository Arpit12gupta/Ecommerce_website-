from django.db import models
from shop.models import Product
from shop.models import User

class Product_ordered(models.Model):
    Product_ordered_ID = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_per_qty = models.DecimalField(max_digits=10, decimal_places=2)
    total_qty = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amt = models.DecimalField(max_digits=20,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return ("Product Ordered id: {}".format(self.Product_ordered_ID))

    class Meta:
        verbose_name_plural = "Product Ordered"