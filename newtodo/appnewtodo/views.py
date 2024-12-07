from django.shortcuts import render, redirect

from appnewtodo.forms import TodoForm
from appnewtodo.models import Todo_data


#
#
# # Create your views here.

def home(request):
    return render(request,'index.html')


def TodoAdd(request):
    form = TodoForm()

    if request.method == 'POST':
        form1 = TodoForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('Todo_view')
    return render(request,"todoadd.html",{"form":form})


def Todo_view(request):
    data = Todo_data.objects.all()
    print(data)
    return render(request,"student_view.html",{"data":data})

def delete_data(request,id):
    data = Todo_data.objects.get(id=id)
    data.delete()
    return redirect("Todo_view")


def update_data(request,id):
    data = Todo_data.objects.get(id=id)
    form = TodoForm(instance= data)
    if request.method == 'POST':
        form1=TodoForm(request.POST,instance=data)
        if form1.is_valid():
           form1.save()
           return redirect("Todo_view")
    return  render(request,'update.html',{"form":form})
