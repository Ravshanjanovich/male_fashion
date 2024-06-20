from django.contrib import admin
from .models import ProductModel, TagModel, Category, BrandModel, SizeModel, ColorModel
from django.utils.safestring import mark_safe
from .forms import ColorForm




@admin.register(ColorModel)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('code',)
    list_display_links = ('code',)
    search_fields = ('code',)
    form = ColorForm

    def color(self, obj):
        free_space = '&nbsp;' * 5
        return mark_safe(f"<div style='background-color:{obj.code};width:200px'>{free_space}</div>")




@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)

@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)

@admin.register(SizeModel)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'long_desc',)
    list_display_links = ('title', 'long_desc',)


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price','discount','created_at', 'sale','brand','category','tags','size',)
#     list_display_links = ('title', 'price', 'created_at',)
#     list_filter = ('created_at',)
#     search_fields = ('title','created_at', 'category', 'brand',)
#     autocomplete_fields = ('category', 'tags', 'size', 'color',)
#     readonly_fields = ("created_at", 'sale',)

#     class Media:
#          js = (
#             'modeltranslation/js/force_jquery.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )   
#          css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }
   
# admin.site.register(ProductAdmin, ProductModel)


    



