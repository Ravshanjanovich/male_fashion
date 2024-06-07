from django.db import models
from django.db.models import Sum
from .abstract import BaseModel
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User





class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("name"))


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Cate'
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


class BrandModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Brending'
        verbose_name = 'Brending'
        verbose_name_plural = 'Breinding'


class SizeModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("name"))


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Size'
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

class ColorModel(models.Model):
    code = models.CharField(max_length=50, verbose_name=_("color"))


    def __str__(self):
        return self.code

    class Meta:
        db_table = 'Colors'
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

class TagModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("tag name"))


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Tags'
        verbose_name = 'Tag'
        verbose_name_plural = "Tags"

class ProductModel(BaseModel):
    title = models.CharField(max_length=40, verbose_name=_("title"))
    short_desc = models.CharField(max_length=150, verbose_name=_("short description"))
    long_desc = models.TextField(verbose_name=_("long description"))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("price"))
    real_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("real price"))
    size = models.ManyToManyField(SizeModel, related_name='product', verbose_name=_('size'))
    brand = models.ForeignKey(BrandModel, on_delete=models.RESTRICT, related_name='product', verbose_name=_("brand"))
    color = models.ManyToManyField(ColorModel, related_name='product', verbose_name=_('color'))
    sale  = models.BooleanField(verbose_name=_("sale"), default=False)
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_("discount"))
    main_image = models.ImageField(upload_to="media/shop_product/%Y/%m/%d", verbose_name=_('image'))
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='product', verbose_name=_("category"))
    tags = models.ManyToManyField(TagModel, related_name='product', verbose_name=_('tags'))


    def __str__(self):
        return f"{self.title},{self.short},{self.brand},{self.tags}"

    class Meta:
        db_table = 'Products'
        verbose_name = "ProductModel"
        verbose_name_plural = "ProductModels"


class WishList(BaseModel):
    user = models.ForeignKey(User , on_delete=models.CASCADE, verbose_name=_("user"), related_name='wishlist')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='wishlist', verbose_name=_('product'))
    

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.product.title}"

    class Meta:
        db_table = 'Wishlist'
        verbose_name = 'Wishlist'
        verbose_name_plural = 'WishLists'
        unique_together = 'user', 'product',


    

