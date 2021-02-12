from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name= "home"),
    path("tienda/", views.tienda, name= "tienda"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
#especificamos el directorio en las url donde se guardan lass img
#se debe importar settings y statics