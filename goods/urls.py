from django.urls import include, path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.CatalogView.as_view(), name='index'),
]
