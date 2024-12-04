from django.contrib import admin

from goods.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "amount", "price", "discount"]
    fields = [
        "name",
        "product_category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "amount",
    ]