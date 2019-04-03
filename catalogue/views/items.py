from django.http import JsonResponse
from django.shortcuts import (
    render, redirect, get_object_or_404)

from catalogue.forms import ItemForm
from catalogue.models import Item, Category


def item_list_rest(request):
    object_list = Item.objects.all()
    data = []

    for i in object_list:
        data.append(
            {'id': i.id,
             'name_short': i.name_short,
             'name_long': i.name_long,
             'description': i.desc,
             'params': i.params,
             'price': i.price,
             'image': i.image.url if i.image else None,
             'category': i.category.name,
             'created': i.created,
             'modified': i.modified,
             }
        )
    return JsonResponse({'results': data})


def item_create(request):
    item_form = ItemForm()
    if request.method == 'POST':
        item_form = ItemForm(
            data=request.POST,
            files=request.FILES)
        if item_form.is_valid():
            item_form.save()
            return redirect('catalogue:main')

    return render(
        request,
        'items/create.html',
        {'item_form': item_form}
    )


def item_list(request):
    return render(
        request,
        'catalogue/index.html',
        {'item_list': Item.objects.all()}
    )


def item_detail(request, pk):
    obj = get_object_or_404(Item, pk=pk)
    return render(
        request,
        'catalogue/detail.html',
        {'object': obj}
    )


def item_update(request, pk):
    obj = get_object_or_404(Item, pk=pk)
    form = ItemForm(
        instance=obj)
    if request.method == 'POST':
        form = ItemForm(
            request.POST,
            files=request.FILES,
            instance=obj)
        if form.is_valid():
            form.save()
            return redirect('products:main')
    return render(
        request,
        'categories/update.html',
        {'form': form}
    )


def item_delete(request, pk):
    obj = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('products:main')
    return render(
        request,
        'categories/delete.html',
        {'object': obj}
    )


def sample(request):
    items_list = Item.objects.all()[:2]
    category_list = Category.objects.all()
    context = {
        'items_list': items_list,
        'category_list': category_list
    }
    return render(
        request,
        'catalogue/index.html',
        context)
