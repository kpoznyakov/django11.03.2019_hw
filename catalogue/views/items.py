from django.shortcuts import render, redirect
from catalogue.forms import CreateItemForm


def create(request):
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
