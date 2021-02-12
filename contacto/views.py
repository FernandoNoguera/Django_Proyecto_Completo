from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage

def contacto(request): 
    contact_form = FormularioContacto()
    if request.method == 'POST': # le estoy diciendo. si se ha hecho post
        contact_form =  FormularioContacto(data=request.POST) #intanciamos los datos ingresados en el form
        if contact_form.is_valid(): #si los datos que ingresé son validos
            nombre = request.POST.get('nombre') #intancia de los datos tomados en el formulario
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            email = EmailMessage("Mensaje desde pag Django",
                                    "El usuario con nombre {} con la dirección {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
                                    "de quien viene el email", 
                                    ['correo.pruebas.desarrollo.200@gmail.com'], 
                                    reply_to=[email], #para responderle a:
                                    )

            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')

            
    context = {'miFormulario': contact_form}
    return render(request, 'contacto/contacto.html',context)
