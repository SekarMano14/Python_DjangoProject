from django.forms import ModelForm
from .models import EmployeeRegister

class EmployeeRegisterForm(ModelForm):
    class Meta:
        model=EmployeeRegister
        fields="__all__"