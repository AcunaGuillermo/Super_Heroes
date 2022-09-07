from django.urls import path
from heroes.views import lista_heroes 

urlpatterns = [
    path('', lista_heroes, name="heroes"),
]