from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from.forms import TodoForm


def index(request):
    form = TodoForm()
    todo_li =Todo.objects.order_by('id')
    contex ={'todo_li': todo_li, 'form' : form}
    return render(request, 'todo/index.html', contex)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text = form.cleaned_data['text'])
        new_todo.save()

    return redirect('index')


def completeTodo(request, todo_id):

    todo = Todo.objects.get(pk = todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')

def uncomplete(request,todo_id):
    todo = Todo.objects.order_by('complete').get(pk = todo_id)
    todo.complete =False
    todo.save()
    return redirect('index')