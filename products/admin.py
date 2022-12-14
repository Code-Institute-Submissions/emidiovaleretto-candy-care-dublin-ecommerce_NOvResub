from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image'
    )
    ordering = ('id',)
    list_display_links = (
        'sku',
        'name',
    )
    list_editable = (
        'price',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class OccasionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'

    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion, OccasionAdmin)
