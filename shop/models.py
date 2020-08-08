from django.db import models
from .constants import (
    GENDER_CHOICES,
    SIZE_CHOICES
)
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='shop/images', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    '''for_gender = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("UNISEX", "Unisex")
    ]
    size = [
        ("Small", "S"),
        ("Medium", "M"),
        ("Large", "L"),
        ("Extra-Large", "XL"),
        ("Extra-Extra-Large", "XXl")

    ]'''
    Product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=255)
    product_description = models.CharField(max_length=1000)
    product_long_description = models.TextField()
    product_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    Gender = models.CharField(max_length=40, choices=GENDER_CHOICES, blank=True, null=True) 
    Sizes = models.CharField(max_length=40, choices=SIZE_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='shop/images/', null=True, blank=True)
    qty_unit = models.IntegerField()
    is_new_arrival = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.product_title

    
    class Meta:
        verbose_name_plural = "Products"


class Contact(models.Model):
    contact_us_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    # subject = models.CharField(max_length=150, default="")
    desc = models.CharField(max_length=500, default="")
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"





class User(AbstractUser):
    mobilenumber = models.CharField(max_length=255, default="")
    profilepicture = models.ImageField('shop/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # signup_type = models.CharField(max_length=20, choices=SIGNUP_CHOICES)
    active = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)
    verified = models.BooleanField(default=True)

    def __str__(self):
        return self.username 

    class Meta:
        verbose_name_plural = "Customers"

class Orders(models.Model):
    # customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    currency = models.CharField(max_length=10,default="INR")
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    reference_order_id = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Orders"

# class Product_ordered(models.Model):
#     Product_ordered_ID = models.AutoField(primary_key=True)
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     price_per_qty = models.DecimalField(max_digits=10, decimal_places=2)
#     total_qty = models.IntegerField()
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_amt = models.DecimalField(max_digits=20,decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return ("Product Ordered id: {}".format(self.Product_ordered_ID))

#     class Meta:
#         verbose_name_plural = "Product Ordered"

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

    class Meta:
        verbose_name_plural = "Order Updates"


class Razorpay(models.Model):
    razorpay_order_id = models.CharField(max_length=200)
    razorpay_payment_id = models.CharField(max_length=200)
    razorpay_signature = models.CharField(max_length=200)

    def __str__(self):
        return "Razorpay Order Id is {}".format(str(self.razorpay_order_id))

    class Meta:
        verbose_name_plural = "Razorpay"


class PayWithRazorpay(models.Model):
    keyid = models.CharField(max_length=50)
    amountPWR = models.IntegerField( default=0)
    currencyPWR = models.CharField(max_length=10,default="INR")
    reference_order_idPWR = models.CharField(max_length=30)
    buttontext = models.CharField(max_length=50)
    CompanyName = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shop/images/', default='shop/images/default.jpeg')
    prefillname = models.CharField(max_length=30)
    prefillemail = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.reference_order_id

    class Meta:
        verbose_name_plural = "Pay With Razorpay"

    
