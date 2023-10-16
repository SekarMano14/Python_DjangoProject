from django import forms

class RegisterForm(forms.Form):
    Firstname=forms.CharField(max_length=15)
    LastName=forms.CharField(max_length=15)
    Email=forms.EmailField()
    MobileNumber=forms.IntegerField()
    Password=forms.CharField(max_length=15)
    Confirm_Password=forms.CharField(max_length=15)

class MyForm(forms.Form):
    name=forms.CharField(max_length=10,min_length=5)
    salary=forms.IntegerField()
    email=forms.EmailField()
    height=forms.DecimalField(max_digits=5,decimal_places=2)
    terms=forms.BooleanField()
    dob=forms.DateField(input_formats=["%Y-%m-%d"])
    time=forms.TimeField()
    gender=forms.ChoiceField(choices=[('M',"Male"),('F','Female'),('O','Others')])
    hobbies=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[("swim","Swim"),
                                                                                   ("Cricket","Cricket"),
                                                                                   ("Bikeride","Bikeride"),
                                                                                   ("Reading Books","Reading Books")])
    Resume=forms.FileField()
    password=forms.CharField(min_length=8,max_length=16,widget=forms.PasswordInput)
    review=forms.CharField(max_length=100,widget=forms.Textarea)
    webistlink=forms.URLField()
    picture=forms.ImageField()

class CustomFiled(forms.Field):
    def validateage(self,value):
        if value<0:
            raise ValueError