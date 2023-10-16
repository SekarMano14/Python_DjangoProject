from django.shortcuts import render

# Create your views here.
from ModelWebApp.models import Studentinfo


def getstudent(request):
    studentinfo=Studentinfo.objects.all()
    student={"studentifo":studentinfo}
    return render(request,"modelapp//studentdetails.html",context=student)
