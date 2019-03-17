from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def cat(request):
    return render(request, 'main/cat.html')


def products_table(request):
    return render(request, 'main/products/table.html')


def products_ball(request):
    return render(request, 'main/products/ball.html')


def products_rackets(request):
    return render(request, 'main/products/rackets.html')
