from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "ProyectoWebApp"

urlpatterns = [
    path("", views.home, name= "home"),
    path("servicios/", views.servicios, name= "servicios"),
    path("tienda/", views.tienda, name= "tienda"),
    path("blog/", views.blog, name= "blog"),
    path("contacto/", views.contacto, name= "contacto"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
#especificamos el directorio en las url donde se guardan lass img
#se debe importar settings y statics