from django.contrib import messages
from django.shortcuts import render


# Create your views here.

def showdata(request):
    return render(request, "allertapp/alertApp.html")


def success(request):
    messages.success(request,"This is Success Message")
    return render(request, "allertapp/alertApp.html")


def error(request):
    messages.error(request,"This is Error Message")
    return render(request, "allertapp/alertApp.html")


def info(request):
    messages.info(request,"This is Just Information Message")
    return render(request, "allertapp/alertApp.html")


def warning(request):
    messages.warning(request,"This is Warning Message")
    return render(request, "allertapp/alertApp.html")
