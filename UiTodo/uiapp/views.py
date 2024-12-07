from django.shortcuts import render, redirect
from uiapp.forms import ModeForm

from uiapp.models import Mode_data


# Create your views here.
def dude(request):
    return render(request,'index.html')

def newin(request):
    return render(request,'newindex.html')

def newadd(request):
    return render(request,'add.html')
def newview(request):
    return render(request,'view.html')
def inter(request):
    return render(request,'interface.html')





def ModeAdd(request):
    form = ModeForm()

    if request.method == 'POST':
        form1 = ModeForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('Mode_view')

    return render(request,"add.html",{"form":form})


def Mode_view(request):
    data = Mode_data.objects.all()
    print(data)
    return render(request,"view.html",{"data":data})

def delete_data(request,id):
    data = Mode_data.objects.get(id=id)
    data.delete()
    return redirect("Mode_view")


def update_data(request,id):
    data = Mode_data.objects.get(id=id)
    form = ModeForm(instance= data)
    if request.method == 'POST':
        form1=ModeForm(request.POST,instance=data)
        if form1.is_valid():
           form1.save()
           return redirect("Mode_view")
    return  render(request,'update.html',{"form":form})

