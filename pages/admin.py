from django.contrib import admin
from pages.models import Contact, Banner

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at',)
    list_display_links = ('name','email',)
    search_fields = ('name','email',)
    list_filter = ('name','email',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('collection','title','sub_title','image','is_active',)
    list_display_links = ('collection','title',)
    search_fields = ('collection','title','sub_title','is_active',)
    list_filter = ('title','collection','is_active',)
