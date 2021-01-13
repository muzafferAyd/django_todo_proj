from django.shortcuts import render

def home(request):
    return render(request, "todo/home.html")


def todo_list(request):
    todos = Todo.object.all()