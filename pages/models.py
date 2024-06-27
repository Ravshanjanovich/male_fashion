from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.abstract import BaseModel

class Contact(BaseModel):
    name = models.CharField(max_length=30, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("email"))
    message = models.TextField( verbose_name=_('message'))

    class Meta:
        verbose_name ='Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name

class Banner(BaseModel):
    collection = models.CharField(max_length=30, verbose_name=_('collection'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    sub_title = models.CharField(max_length=150, verbose_name=_('subtitle'))
    image = models.ImageField(upload_to="banner/Y%/m%/%d", verbose_name=_('image'))
    is_active = models.BooleanField(default=False, blank=True, verbose_name=_("is active"))


    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = "Banners"


class MapsModel(models.Model):
    maps = models.URLField()

    class Meta:
        verbose_name = 'Maps'
        verbose_name_plural = "Mapses"


