from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Customer
from .models import Item


# Create your views here.
def ecommerce(request):
    items = Item.objects.all()
    return render(request, 'ecommerce/home.html', {'items': items})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user, name=user.username)  # Creazione del profilo Customer
            login(request, user)  # Autenticare l'utente dopo la registrazione
            return redirect('ecommerce')  # Reindirizzare alla home page o a un'altra pagina
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
