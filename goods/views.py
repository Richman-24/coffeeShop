from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from goods.models import Category, Product


class CatalogView(ListView):
    template_name = "base.html"
    paginate_by = 6
    model = Category

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()

        return context


class ProductView(DetailView):
    template_name = "product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"
    model = Product
