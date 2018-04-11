from django.forms import ModelForm

from . import models

# Django sigue el filosofía DRY (Dont Repeat Yourself),
# no te repitas. así define classes abstractas para
# manejar métodos comunes en una aplicación
    

class ToDoForm(ModelForm):
   
    class Meta:
        model = models.ToDo
        fields = ['name', 'tags']

