from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from goods.models import Category, Product


class CatalogView(ListView):
    template_name = "goods/catalog.html"
    paginate_by = 3
    context_object_name = "products"
    model = Product
    
    def get_queryset(self) -> QuerySet[Any]:
        category_slug = self.kwargs.get("category_slug")

        if category_slug == 'all' or category_slug is None:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(category__slug=category_slug)
        return queryset
        

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["slug_url"] = self.kwargs.get("category_slug")
        return context


class ProductView(DetailView):
    template_name = "product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"
    model = Product
