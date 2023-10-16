from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id=models.IntegerField()
    employee_name=models.CharField(max_length=15)
    mobile_no=models.IntegerField()
    salary=models.IntegerField()

    def __str__(self):
        return self.employee_name



class Studentinfo(models.Model):
    student_id=models.IntegerField()
    student_name=models.CharField(max_length=15)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    course=models.CharField(max_length=10)
    Trainer=models.CharField(max_length=10)
    fees=models.IntegerField()

    def __str__(self):
        return self.student_name

