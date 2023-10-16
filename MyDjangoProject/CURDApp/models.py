from django.db import models

# Create your models here.
class EmployeeRegister(models.Model):
    employee_id=models.IntegerField()
    employee_name=models.CharField(max_length=15)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    salary=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.employee_name
