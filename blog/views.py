from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada 

import os

def muestrainicio(request):
    return render_to_response('Inicio.html',
                              {},
                              RequestContext(request))

# Create your views here.

def verbtnmg(request):
    return render_to_response('cambiolugar.html',
                              {},
                              RequestContext(request))
# Create your views here.

def vercal(request):
    return render_to_response('Calculadora.html',
                              {},
                              RequestContext(request))
# Create your views here.

def vercon(request):
    return render_to_response('Contactos.html',
                              {},
                              RequestContext(request))
# Create your views here.

def verconv(request):
    return render_to_response('conversor.html',
                              {},
                              RequestContext(request))
# Create your views here.

def vercro(request):
    return render_to_response('cronometro.html',
                              {},
                              RequestContext(request))
# Create your views here.

def verimagen(request):
    return render_to_response('Image.html',{},RequestContext(request))

def vernoticias(request):
    context = RequestContext(request)
    posts = Entrada.objects.all()
    return render_to_response('noticias.html',{'posts':posts},context)

def ver_post(request, id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id=id_post)
    return render_to_response('post.html',{'post':mi_post},context)
