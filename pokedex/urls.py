from pokedex import views
from django.urls import path

app_name = "pokedex"
urlpatterns = [
    path("", views.listar_pokemon, name="listar_pokemon"),
    path("crear/", views.crear_pokemon, name="crear_pokemon")
]
