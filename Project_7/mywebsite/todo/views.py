from django.shortcuts import render, redirect
from .forms import todoForm
from .models import Todo
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    mytodo = Todo.objects.order_by('created_at')

    form = todoForm()

    context = {
        'mytodo': mytodo,
        'form': form
    }

    return render( request, 'todo/index.html', context)

@require_POST
def addNewtodo(request):
    form = todoForm(request.POST)
    if form.is_valid:
        my_new_todo = Todo( todoText = request.POST['text'])
        my_new_todo.save()
    
    return redirect('index')

def completeTodo(request, todoID):
    mytodo = Todo.objects.get( pk = todoID)
    mytodo.complete = True
    mytodo.save()

    return redirect('index')

def deleteTodo(request):
    Todo.objects.filter(complete__exact = True).delete()

    return redirect('index')

def clearAll(request):
    Todo.objects.all().delete()
    return redirect('index')