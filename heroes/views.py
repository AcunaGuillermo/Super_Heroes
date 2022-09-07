from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from heroes.models import superHeroes

def inicio(request):
    return render(request, "heroes/inicio.html")

def lista_heroes(request):
    queryset = superHeroes.objects.all()
    diccionario = {'heroes':queryset}
    plantilla = loader.get_template('heroes/heroes_list.html')
    documento_html = plantilla.render(diccionario)
    
    return HttpResponse(documento_html)

def get_heroe(request, id):
    heroe = superHeroes.objects.get(id=id)
    diccionario = {'heroe':heroe}
    plantilla = loader.get_template('heroes/heroe.html')
    documento_html = plantilla.render(diccionario)
    
    return HttpResponse(documento_html)
