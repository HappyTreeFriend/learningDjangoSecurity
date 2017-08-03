# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import request

# Create your views here.

from django.http import JsonResponse
def returnJSON(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28,
        'html': '", }<script>alert(1)</script>{"a":"',
    }
    return JsonResponse(data)


import json
from django.http import HttpResponse
def returnJSON2(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28,
        'html': '", }<script>alert(1)</script>{"a":"',
    }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')

def returnJS(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28,
        'html': '", }<script>alert(1)</script>{"a":"',
    }
    return render(request, 'returnJS.html', {'data':data})