from django.urls import include, path

from goods import views

app_name = 'catalog'

urlpatterns = [
    path('<slug:category_slug>/', views.CatalogView.as_view(), name='index'),
    path('catalog/<slug:category_slug>/', views.CatalogView.as_view(), name='index'),
    path('product/<slug:product_slug>/', views.ProductView.as_view(), name='product'),
]
