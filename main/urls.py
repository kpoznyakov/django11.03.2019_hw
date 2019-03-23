from django.urls import path

from .views import main, contacts

app_name = 'main'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', main, name='main'),
]