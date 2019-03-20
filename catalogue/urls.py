from django.urls import path

from .views import product_list, product_detail

app_name = 'catalogue'

urlpatterns = [
    path('detail/', product_detail, name='detail'),
    path('', product_list, name='main'),
]