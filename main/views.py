from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def uppercase_first_symb(string=str()):
    return string.capitalize()
