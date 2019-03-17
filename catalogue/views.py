from django.shortcuts import render
import json


# Create your views here.


def product_list(request):
    return render(request,
                  'catalogue/index.html',
                  items
                  )


def product_detail(request):
    return render(request, 'catalogue/detail.html')


with open('static/items.json', 'r') as f:
    items = json.load(f)

# def code_test(request):
#     return render(request,
#                   'code_test/index.html',
#                   {
#                       'current_time': current_time(),
#                       'sum11': 1 + 1,
#                       'some_list': ['String Item',
#                                     {
#                                         'Dict item value int()': 1,
#                                         'Dict item value str())': '',
#                                         'Dict item value bool()': True,
#                                         'Dict item value None': None,
#                                     },
#                                     123456,
#                                     True,
#                                     None
#                                     ]
#                   },
#                   )
