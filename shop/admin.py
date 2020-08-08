from django.contrib import admin

from . models import (
    Product,
    Category,
    Contact,
    Orders,
    User,
    OrderUpdate, 
    Razorpay,
    PayWithRazorpay

    )

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contact)
# admin.site.register(Orders)
admin.site.register(User)
admin.site.register(OrderUpdate)
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'email','amount')

admin.site.register(Razorpay)
admin.site.register(PayWithRazorpay)