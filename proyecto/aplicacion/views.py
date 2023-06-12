from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios


# Create your views here.
def index_aplicacion(request):
    data=Usuarios.objects.all()
    context=dict(usuarios=data[0])
     
    
    
    return render(request,"index.html", {"context":context})
