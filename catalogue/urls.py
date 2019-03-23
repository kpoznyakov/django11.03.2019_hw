from django.urls import path

from .views import product_list, product_detail, category_create

app_name = 'catalogue'

urlpatterns = [
    path('<int:pk>/', product_detail, name='detail'),
    path('', product_list, name='main'),
    path('create/', category_create, name='create'),
]
