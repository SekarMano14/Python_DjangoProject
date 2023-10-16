from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import EmployeeRegisterForm
from .models import EmployeeRegister


# Create your views here.
def getemployeeDetails(request):
    empdetails = EmployeeRegister.objects.all()
    data = serializers.serialize("json", empdetails)
    # return HttpResponse(data,content_type="application/json")
    return render(request, "curdapp//employeedetails.html", context={"empdetails": empdetails})


def createnew_employee(request):
    form = EmployeeRegisterForm()
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                "<h1>The Employee Data Successfully Add to Database..<a href='/curd/employeedetails/'>Click here See All Employee datas</a></h1>")
    return render(request, "curdapp//addemployee.html", context={"form": form})


def delete_employee(request, id):
    empdetails = EmployeeRegister.objects.get(id=id)
    empdetails.delete()
    return redirect("/home")
    # return HttpResponse(
    #     "<h1>The Employee Data Successfully Deleted from Database..<a href='/curd/employeedetails/'>Click here See All Employee datas</a></h1>")


def update_employee(request, id):
    empdetails = EmployeeRegister.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST, instance=empdetails)
        if form.is_valid():
            form.save()
            return HttpResponse(
                "<h1>The Employee Data Successfully Updated from Database..<a href='/curd/employeedetails/'>Click here See All Employee datas</a></h1>")
    return render(request, "curdapp//updateemployee.html", context={"employee": empdetails})
