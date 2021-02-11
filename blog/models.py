from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria' #nombre que tendra esta clase en la base de datos
        verbose_name_plural = 'categorias' #nombre que tendra esta clase en plural dentro de  la base de datos

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True )
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post' #nombre que tendra esta clase en la base de datos
        verbose_name_plural = 'posteos' #nombre que tendra esta clase en plural dentro de  la base de datos

    def __str__(self):
        return self.titulo

