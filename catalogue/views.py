from django.shortcuts import render, redirect
from .models import Category, Item
from .forms import CreateCategoryForm, CreateCategoryModelForm, CreateItemForm


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


# def category_create(request):
#     form = CreateCategoryForm()
#     if request.method == 'POST':
#         form = CreateCategoryForm(data=request.POST)
#         if form.is_valid():
#             Category.objects.create(
#                 name=form.cleaned_data.get('name')
#             )
#             return redirect('catalogue:main')
#
#     return render(
#         request,
#         'categories/create.html',
#         {'form': form}
#     )

def category_create(request):
    form = CreateCategoryModelForm()
    if request.method == 'POST':
        form = CreateCategoryModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue:main')

    return render(
        request,
        'categories/create.html',
        {'form': form}
    )


def item_create(request):
    item_form = CreateItemForm()
    if request.method == 'POST':
        item_form = CreateItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item_form.save()
            return redirect('catalogue:main')

    return render(
        request,
        'items/create.html',
        {'item_form': item_form}
    )
