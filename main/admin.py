from django.contrib import admin

from . import models

# Aqui el patrón decorador que recibe un modelo
# y lo registra en el adminitrador de django para poder
# hacer los métodos CRUD


@admin.register(models.ToDo)
class ToDoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass
