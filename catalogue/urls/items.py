from django.urls import path

from catalogue.views import (item_create, item_detail,
                             item_list, item_update, item_delete, item_list_rest)

app_name = 'items'

urlpatterns = [
    path('create/', item_create, name='create'),
    path('<int:pk>/update/', item_update, name='update'),
    path('<int:pk>/delete/', item_delete, name='delete'),
    path('<int:pk>/', item_detail, name='detail'),
    path('', item_list, name='main'),
    # path('', sample, name='all_list'),
]


urlpatterns += [
    path('api/', item_list_rest, name='rest_list')
]