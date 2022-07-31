from django.contrib import admin
from db.models import Products


class ProductsAdmin(admin.ModelAdmin):

    list_display = ['name', 'price', 'presence', 'author']


admin.site.register(Products, ProductsAdmin)
