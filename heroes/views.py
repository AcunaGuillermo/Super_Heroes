from http.client import HTTPResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from heroes.models import superHeroes

def lista_heroes(request):
    queryset = superHeroes.objects.all()
    diccionario = {'heroes':queryset}
    plantilla = loader.get_template('heroes_list.html')
    documento_html = plantilla.render(diccionario)
    return HTTPResponse(documento_html)
# Create your views here.
