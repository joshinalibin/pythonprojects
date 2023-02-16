from django.shortcuts import render

# Create your views here.
from .models import place
from .models import persons

def demo(request):
     obj=place.objects.all()
     obj1=persons.objects.all()
     return render(request,"index.html",{'result':obj,'res':obj1})



