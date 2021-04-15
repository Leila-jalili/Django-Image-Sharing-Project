from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import ToDo 
from .forms import ToDoForm

# Create your views here.
def todos_view(request):
    todos=ToDo.objects.all()
    #todos=ToDo.objects.all().order_by("id")
    #todos=ToDo.objects.filter(id=2)
    return HttpResponse(todos)


def todo_view(request, id): 
    #todo=ToDo.objects.filter(id=id)
    todo=get_object_or_404(ToDo, pk=id)
    #if todo.exists():
     #   todo=todo[0]
    #return HttpResponse(f"<h1 style='font-size:4rem'>{todo.name}</h1>")
    return render(request, "todo.html", {"todo":todo, "items":todo.item_set.all()})
    #else:
      #  return HttpResponseNotFound()
    #return HttpResponse("Todo " + str(id))   

def todo_create_view(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/todo/list")
        else:
            return render(request, "todo_create.html", {"form": form})    

        pass
    else:
        form = ToDoForm()
    return render(request, "todo_create.html", {"form": form})    