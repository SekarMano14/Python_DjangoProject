from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . import forms
from .models import RegisterModel


def register(request):
    form = forms.RegisterForm()
    return render(request, "formapp//register.html", context={"form": form})


def userregister(request):
    if request.method == 'POST':
        if (request.POST.get("Firstname") and request.POST.get("LastName") and request.POST.get(
                "Email") and request.POST.get("MobileNumber") and request.POST.get("Password")
                and request.POST.get(
                "Confirm_Password")):
            reg = RegisterModel()
            reg.Firstname = request.POST.get("Firstname")
            reg.LastName = request.POST.get("LastName")
            reg.Email = request.POST.get("Email")
            reg.MobileNumber = request.POST.get("MobileNumber")
            reg.Password = request.POST.get("Password")
            reg.Confirm_Password = request.POST.get("Confirm_Password")
            reg.save()
            return HttpResponse("Success fully registerd")
        else:
            return HttpResponse("Some fileds are missing")

    form = forms.RegisterForm()
    return render(request, "formapp//register.html", context={"form": form})

def getalldetails(request):
    registerdetails=RegisterModel.objects.all()
    return render(request,"formapp//result.html",context={"register":registerdetails})

def allform(request):
    form=forms.MyForm()
    return render(request, "formapp//allform.html", context={"form": form})
