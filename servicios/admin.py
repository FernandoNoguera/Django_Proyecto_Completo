from django.contrib import admin

from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #para que muestre esos campos a modo de lectura en el admin 

admin.site.register(Servicio, ServicioAdmin)
 