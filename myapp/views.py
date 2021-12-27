from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import ListForm
from .models import List

def add(request):
    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = ListForm()
            except:
                pass

    datas = List.objects.all()
    return render(request,'index.html',{'datas':datas,'form':form})

def update(request,id=0):
    if request.method == 'POST':
        data = List.objects.get(pk=id)
        form = ListForm(request.POST,instance=data)
        if form.is_valid:
            try:
                form.save()
                return redirect('/add')
            except:
                pass
    else:
        data = List.objects.get(id=id)
        allData = List.objects.all()
        form = ListForm(instance=data)
        return render(request,'update.html',{'datas':allData,'form':form,'updateData':data})
    
def delete(request,id=0):
    data = List.objects.get(id=id)
    data.delete()
    return redirect('/add')
    

