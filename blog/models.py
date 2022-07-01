from contextlib import nullcontext
from tokenize import blank_re
from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    contenido = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.title}, author: {self.author}, contenido: {self.contenido}, fecha_creacion: {self.fecha_creacion}'