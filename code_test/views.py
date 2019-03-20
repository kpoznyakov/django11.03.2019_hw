from django.shortcuts import render

import datetime


# Create your views here.


def code_test(request):
    return render(request,
                  'code_test/index.html',
                  {
                      'current_time': current_time(),
                      'sum11': 1 + 1,
                      'some_list': ['String Item',
                                    {
                                        'Dict item value int()': 1,
                                        'Dict item value str())': '',
                                        'Dict item value bool()': True,
                                        'Dict item value None': None,
                                    },
                                    123456,
                                    True,
                                    None
                                    ]
                  },
                  )
    # return render(request, 'code_test/index.html')


def current_time():
    return str(datetime.datetime.now())
