import datetime

from django.shortcuts import render

# Create your views here.
def ipltable(request):
    now = datetime.datetime.now()
    details={"name":"Manoj","country":"India","location":"Chennai","date":now}
    return render(request,"secondwebapp//ipltable.html",context=details)

def getprice(request):
    return render(request,"secondwebapp//getproductdetails.html")


def totalPrice(request):
    mobile=int(request.GET["mobile"])
    laptop=int(request.GET["laptop"])
    tablet=int(request.GET["tablet"])
    keyboard=int(request.GET["keyboard"])
    totaprice=mobile+laptop+tablet+keyboard
    price={"total":totaprice}
    return render(request, "secondwebapp//result.html",context=price)

