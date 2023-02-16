from django.shortcuts import render, redirect
from.models import Fashion
from.forms import FashionForm
# Create your views here.
def index(request):
    fashion=Fashion.objects.all()
    return render(request,"index.html",{'fashion_list':fashion})

def detail(request,fashion_id):
    fashion=Fashion.objects.get(id=fashion_id)
    return render(request,"detail.html",{'fashion':fashion})

def add(request):
    if request.method=="POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        fashion=Fashion(name=name,price=price,category=category,desc=desc,img=img)
        fashion.save()
        return redirect('/')
    return render(request,"add.html")

def update(request,id):
    fashion = Fashion.objects.get(id=id)
    form = FashionForm(request.POST or None,request.FILES,instance=fashion)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form,'fashion':fashion})

def delete(request,id):
    if request.method=="POST":
       fashion=Fashion.objects.get(id=id)
       fashion.delete()
       return redirect('/')
    return render(request,"delete.html")