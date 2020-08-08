'''from django.db import models
from datetime import datetime
from users.models import CustomUser
from .constants import (
    ORDER_STATUS_CHOICES,
    ORDER_SOURCE_CHOICES,
    TRANSACTION_STATUS_CHOICES
)

class Order(models.Model):
    # order_sources = [
    #     ("iOS", "iOS"),
    #     ("ANDROID", "Android"),
    #     ("WEB", "Web")
    # ] 
    # Order_status = [
    #     ("INCOMPLETE", "Incomplete"),
    #     ("PLACED", "Placed"),
    #     ("ON_HOLD", "On Hold"),
    #     ("SHIPPED","Shipped"),
    #     ("OUT_FOR_DELIVERY","Out for Delivery"),
    #     ("DELIVERED","Order Delivered"),
    #     ("CANCELED","Order Cancelled"),
    # ] 
    # Transaction_status = [
    #     ("FAILED", "Transaction Failed"),
    #     ("SUCCESS", "Transaction Success"),
    #     ("CANCELLED", "Transaction Cancelled"),
    #     ("REFUNDED","Money Refunded"),
        
    # ] 
    order_id = models.AutoField(primary_key=True)
    # order_date = models.DateField(default=datetime.date.today)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_count = models.IntegerField()
    total_product_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_source = models.CharField(max_length=30, choices=ORDER_SOURCE_CHOICES)
    source_info = models.CharField(max_length=100)
    transaction_id = models.IntegerField()
    transaction_type = models.CharField(max_length=100)
    transaction_status = models.CharField(max_length=30, choices=TRANSACTION_STATUS_CHOICES)
    order_status = models.CharField(max_length=30, choices=ORDER_STATUS_CHOICES)

    
    def __str__(self):
        return ("{}'s Order no. {}".format(self.customer, self.order_id))

    
    class Meta:
        verbose_name_plural = "Orders"'''