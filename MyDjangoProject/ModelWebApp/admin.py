from django.contrib import admin

# Register your models here.
from .models import Employee, Studentinfo

admin.site.register(Employee)
admin.site.register(Studentinfo)
