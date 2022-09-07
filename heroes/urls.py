from django.urls import path
from heroes.views import lista_heroes, get_heroe

urlpatterns = [
    path('', lista_heroes, name="heroes"),
    path('<int:id>/', get_heroe, name="heroe")
]