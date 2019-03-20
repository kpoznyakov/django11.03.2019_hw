from django.shortcuts import render
from .models import Category, Item


# Create your views here.


def product_list(request):
    return render(
        request,
        'catalogue/index.html',
        {'object_list': Item.objects.all()}
    )


def product_detail(request, pk):
    return render(
        request,
        'catalogue/detail.html',
        {'object': Item.objects.get(id=pk)}
    )
