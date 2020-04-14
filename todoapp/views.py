from django.shortcuts import render, HttpResponseRedirect
from .models import ToDo


def index(request):
    todas_atvdds = ToDo.objects.all()
    return render(request, 'home/index.html', {'todo_items': todas_atvdds})


def AddTodo(request):
    novo_item = ToDo(text=request.POST["text"])
    novo_item.save()
    return HttpResponseRedirect('/todo')


def deleteTodo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/todo')



