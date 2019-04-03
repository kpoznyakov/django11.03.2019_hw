from django.shortcuts import render, redirect, get_object_or_404

from catalogue.forms import CreateCategoryModelForm
from catalogue.models import Category


# Create your views here.


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
        form = CreateCategoryModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogue:main')

    return render(
        request,
        'categories/create.html',
        {'form': form}
    )


def category_update(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    form = CreateCategoryModelForm(
        instance=obj
    )
    if request.method == 'POST':
        form = CreateCategoryModelForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return redirect('catalogue:main')
    return render(
        request,
        'categories/update.html',
        {'form': form}
    )


def category_delete(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('catalogue:main')
    return render(
        request,
        'categories/delete.html',
        {'object': obj}
    )


def category_list(request):
    return render(
        request,
        'catalogue/index.html',
        {'category_list': Category.objects.all()}
    )


def category_detail(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    return render(
        request,
        'categories/detail.html',
        {'object': obj}
    )
