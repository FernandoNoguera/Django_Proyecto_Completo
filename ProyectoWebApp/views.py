from django.shortcuts import render, HttpResponse

from servicios.models import Servicio

def home(request):
    return render(request, 'ProyectoWebApp/home.html')

def servicios(request):
    servicios = Servicio.objects.all()#se le indica q taiga los servivios de la base de datos
    print(servicios)
    context = {'servicios':servicios}

    return render(request, 'ProyectoWebApp/servicios.html', context)


def tienda(request):
    return render(request, 'ProyectoWebApp/tienda.html')


def blog(request):
    return render(request, 'ProyectoWebApp/blog.html')


def contacto(request):
    return render(request, 'ProyectoWebApp/contacto.html')

