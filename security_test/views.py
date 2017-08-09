# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import request, HttpResponse, JsonResponse
import json


# Create your views here.
# TODO:JSON/JAVASCRIPT的XSS防御
def returnJSON(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28,
        'html': '", }<script>alert(1)</script>{"a":"',
    }
    return JsonResponse(data)


def returnJS(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28,
        'html': '", }<script>alert(1)</script>{"a":"',
    }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/javascript')


def returnHTML(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28,
        'html': '", }<script>alert(1)</script>{"a":"',
    }
    return render(request, 'returnJS.html', {'data': data})