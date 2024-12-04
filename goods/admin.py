from django.contrib import admin

from goods.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {"slug":("name",)}
        list_display = ["name",]