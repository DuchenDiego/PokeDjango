from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def login_user(request):
    user = authenticate(
        username = request.POST['username'],
        password = request.POST['password']
    )
    if user is not None :
        print(type(user))
        login(request, user) # Crea sesion 
        return HttpResponseRedirect(reverse('pokedex:listar_pokemon'))
    else:
        return HttpResponse('No existe usuario', status=403)

def login_view(request):
    return render(request, 'authentication/login.html') 
