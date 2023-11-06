from django.contrib import admin
from .models import Product, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'quantity']
    list_editable = ['price', 'quantity']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
