from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader

from .models import Book


def rot(request):
    template = loader.get_template('index.html')
    s = "Ну давай же"
    context2 = {'s': s}
    b = Book.objects.order_by('title')
    context = {'b':b,'s':s}
    return HttpResponse(template.render(context, request))

# Create your views here.
