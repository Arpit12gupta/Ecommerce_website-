from django.db import models
from .constants import(
    SIGNUP_CHOICES
)

# Create your models here.
class CustomUser(models.Model):
    # username = None
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    '''signup = [
        ("CUSTOM", "Custom"),
        ("FACEBOOK", "Facebook"),
        ("GOOGLE", "Google")
    ]'''
    name = models.CharField(max_length=30, null=True, blank=True)
    # email = models.EmailField()
    mobile_number = models.CharField( max_length=255, blank=False)
    dp_image = models.ImageField(upload_to='uploads/',  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    signup_type = models.CharField(max_length=20, choices=SIGNUP_CHOICES)
    active = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)
    verified = models.BooleanField(default=True)

    def __str__(self):
        return ("Customer Name : {}".format(self.email))

    class Meta:
        verbose_name_plural = "Customers"