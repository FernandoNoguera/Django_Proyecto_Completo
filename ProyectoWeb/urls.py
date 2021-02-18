from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('ProyectoWebApp.urls')),
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda', include('tienda.urls')),
]
