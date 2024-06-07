from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from shop import models
from django.db import IntegrityError






def is_discount(self):
    return bool(self.discount)

def new(self):
    return (timezone.now() - self.created_at()).days <= 7

@staticmethod
def get_cart_info (self):
    cart = request.session.get("cart" , [])
    if not cart:
        return  0, 0.0
    return len(cart), ProductModel.objects.filter(id__in=cart).aggregate(Sum("real_price"))

@staticmethod
def get_cart_objects(self):
    cart = request.objects.get('cart', [])
    if not cart:
        return None
    return ProductModel.objects.filter(id__in=cart)

@staticmethod
def created_or_delete(user, product):
    try:
        return WishList.objects.create( user=user, product=product)
    except IntegrityError:
        return WishList.objects.get( user=user , product=product)
        



