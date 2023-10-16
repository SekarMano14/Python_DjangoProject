import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyDjangoProject.settings")

import django

django.setup()

from CURDApp.models import EmployeeRegister
from faker import Faker
from random import *

faker = Faker()
def fakeemployeedatas():
    f_empid = randint(200, 999)
    f_name = faker.name()
    f_phnoe = randint(7000000000, 9000000000)
    f_address = faker.city()
    f_salary = randint(20000, 50000)
    f_email = faker.email()
    emp = EmployeeRegister.objects.get_or_create(employee_id=f_empid,
                                                 employee_name=f_name,
                                                 phone=f_phnoe,
                                                 address=f_address,
                                                 salary=f_salary, email=f_email)


# for i in range(0,10):
#     fakeemployeedatas()

import calendar
yy=2023
mm=9

print(calendar.month(yy,mm))