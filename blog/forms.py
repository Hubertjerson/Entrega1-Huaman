import re
from django import forms


class formBlog(forms.Form):
    title = forms.CharField(max_length=50)
    author= forms.CharField(max_length=50)
    contenido = forms.CharField(max_length=50)
    fecha_creacion = forms.DateTimeField(required=False)

class busquedaAuthor(forms.Form):
    author = forms.CharField(max_length=50,required=False)