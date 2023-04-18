from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PersonForm
from .models import Details


# Create your views here.
def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


def formdata(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            account_type = form.cleaned_data['account_type']
            district = form.cleaned_data['district']
            branch = form.cleaned_data['branch']
            materials = ', '.join(form.cleaned_data['materials_required'])
            details = Details(name=name, dob=dob, age=age, gender=gender, phone_number=phone_number, email=email,
                              address=address, account_type=account_type,district=district,branch=branch,
                              materials_required=materials)
            details.save()
            messages.info(request, "Application Accepted")
            return redirect('formdata')
    else:
        form = PersonForm()
    return render(request, 'form.html', {'form': form})
