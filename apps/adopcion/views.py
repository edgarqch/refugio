# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_adopcion(request):
    return HttpResponse("Soy la pagina principal de la aplicacion adopcion")