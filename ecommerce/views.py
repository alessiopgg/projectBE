from django.shortcuts import render
from .models import Item


# Create your views here.
def ecommerce(request):
    items = Item.objects.all()
    return render(request, 'ecommerce/index.html', {'items': items})
