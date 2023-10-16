from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    Firstname=models.CharField(max_length=15)
    LastName=models.CharField(max_length=15)
    Email=models.EmailField()
    MobileNumber=models.IntegerField()
    Password=models.CharField(max_length=15)
    Confirm_Password=models.CharField(max_length=15)

    def __str__(self):
        return self.Firstname