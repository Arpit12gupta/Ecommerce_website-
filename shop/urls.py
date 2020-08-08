from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index , name="shophome" ),
    path('about/', views.about, name="about"),
    path("products/<int:Product_id>", views.productView, name = "ProductView"),
    path('contact/',views.contact, name = 'contact'),
    path("checkout/", views.checkout, name="Checkout"),
    path('signup/', views.handleSignup, name='handleSignup'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('checkout_summary/', views.checkout_summary, name='checkout_summary'),
    path('tracker/', views.tracker, name='tracker'),
    path("checkout/payment/success/", views.handlerazorpay, name = 'handlerazorpay')

]