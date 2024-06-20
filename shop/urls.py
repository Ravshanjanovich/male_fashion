from django.urls import path
from shop.views import Shop


urlpatterns = [
    path('', Shop.as_view(), name='shop'),
]
