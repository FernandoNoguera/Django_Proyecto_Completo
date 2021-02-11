from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio' #nombre que tendra esta clase en la base de datos
        verbose_name_plural = 'servicios' #nombre que tendra esta clase en plural dentro de  la base de datos

    def __str__(self):
        return self.titulo


