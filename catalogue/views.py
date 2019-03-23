from django.shortcuts import render, redirect
from .models import Category, Item
from .forms import CreateCategoryForm


# Create your views here.


def product_list(request):
    return render(
        request,
        'catalogue/index.html',
        {'object_list': Item.objects.all(),
         'category_list': Category.objects.all()
         }
    )


def product_detail(request, pk):
    return render(
        request,
        'catalogue/detail.html',
        {'object': Item.objects.get(id=pk)}
    )


def category_create(request):
    form = CreateCategoryForm()
    if request.method == 'POST':
        Category.objects.create(
            name=request.POST.get('name'),
        )
        return redirect('catalogue:main')

    return render(
        request,
        'categories/create.html',
        {'form': form}
    )
