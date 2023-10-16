from django.db import models

# Create your models here.

class UserRegister(models.Model):
    username=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=16)

    def __str__(self):
        return self.username