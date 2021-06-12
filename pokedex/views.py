from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Pokemon
from .forms import CrearPokemonForm

# Create your views here.

def listar_pokemon(request):
    pokemons = Pokemon.objects.all()
    context = {
            'lista_pokemons': pokemons,
            'crear_form': CrearPokemonForm()
        }
    return render(request, 'pokedex/index.html', context)

def crear_pokemon(request):
    if request.method == 'POST':
        form = CrearPokemonForm(request.POST)
        if form.is_valid():
            pokemon = Pokemon(
                IDpoke = form.IDpoke,
                Descripcion = form.Descripcion,
                Peso = form.Peso,
                Altura = form.Altura
            )
            pokemon.save()
        return HttpResponseRedirect(reverse('pokedex:listar_pokemon'))