from django.urls import path

from .views import product_list, product_detail, category_create, item_create

app_name = 'catalogue'

urlpatterns = [
    path('create/', category_create, name='create'),
    path('<int:pk>/', product_detail, name='detail'),
    path('', product_list, name='main'),
    path('item_create/', item_create, name='item_create'),

]
