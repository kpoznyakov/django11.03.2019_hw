from django.urls import path

from .views import code_test

app_name = 'code_test'

urlpatterns = [
    path('', code_test, name='main'),
]