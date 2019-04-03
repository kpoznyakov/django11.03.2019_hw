from django.urls import path

from catalogue.views import create

app_name = 'items'

urlpatterns = [
    path('create/', create, name='create')
]
