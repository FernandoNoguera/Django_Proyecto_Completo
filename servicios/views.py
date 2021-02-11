from django.shortcuts import render

from servicios.models import Servicio

def servicios(request):
    servicios = Servicio.objects.all()#se le indica q taiga los servivios de la base de datos
    print(servicios)
    context = {'servicios':servicios}
    return render(request, 'servicios/servicios.html', context)

