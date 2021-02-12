from django.shortcuts import render

from .forms import FormularioContacto

def contacto(request): 
    contact_form = FormularioContacto()
    context = {'miFormulario': contact_form}
    return render(request, 'contacto/contacto.html',context)
