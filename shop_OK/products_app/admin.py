from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    save_on_top = True
    fields = ('number', 'name', 'slug', 'category', 'description', 'photo',  'created', 'updated',
              'stock', 'price', 'available')
    list_display = ('number', 'name', 'slug', 'category', 'description', 'get_photo',  'created', 'updated',
              'stock', 'price', 'available')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "Фото не установлено"

    get_photo.short_description = 'Миниатюра'


admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryProduct, ProductCategoryAdmin)