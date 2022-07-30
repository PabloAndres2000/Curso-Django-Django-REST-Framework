from django.contrib import admin

from store.apps.products.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    User model admin.
    """

    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    User model admin.
    """

    list_display = ('name', 'price', 'stock', 'is_available',)


