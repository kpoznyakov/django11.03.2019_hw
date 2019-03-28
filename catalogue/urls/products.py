from django.urls import path

from catalogue.views import product_list, product_detail, category_create, category_update, category_delete

app_name = 'catalogue'

urlpatterns = [
    path('create/', category_create, name='create'),
    path('<int:pk>/update/', category_update, name='update'),
    path('<int:pk>/delete/', category_delete, name='delete'),
    path('<int:pk>/', product_detail, name='detail'),
    path('', product_list, name='main')
]
