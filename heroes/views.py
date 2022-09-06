from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from heroes.models import superHeroes

def lista_heroes(request):
    queryset = superHeroes.objects.all()
    diccionario = {'heroes':queryset}
    plantilla = loader.get_template('heroes_list.html')
    documento_html = plantilla.render(diccionario)
    
    return HttpResponse(documento_html)