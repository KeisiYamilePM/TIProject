from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from . import forms, models

# Vista home que sirve como controlador que usa el modelo ToDo

# y con el template home.html    
# En django MVC es MTV
# Model => ToDo
# Template => home.html
# View => funcion home

def home(request):
    
    to_dos = models.ToDo.objects.all()

    return render(request, 'main/home.html', locals())


@require_http_methods(['GET', 'POST'])
def new_todo(request):

    if request.method == 'GET':
        todo_form = forms.ToDoForm()
    else:
        todo_form = forms.ToDoForm(data=request.POST)
        if todo_form.is_valid():
            todo = todo_form.save()
            return redirect('/')

    return render(request, 'main/new_todo.html', locals())


def change_status(request):
    to_do_pk = request.GET.get('to_do_pk')
    status = request.GET.get('status')

    to_do = get_object_or_404(models.ToDo, pk=to_do_pk)
    to_do.status = status
    to_do.save()
    return redirect('/')
