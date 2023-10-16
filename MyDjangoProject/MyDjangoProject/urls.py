"""
URL configuration for MyDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from FirstWebApp import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.homepage),
    path('home/',v1.homepage),
    path('login/',v1.loginpage),
    path('register/',v1.registerpage),
    path('second/',include("SecondWebApp.urls")),  #http://127.0.0.1.8000/second/ipltable
    # path('',include("SecondWebApp.urls")), #http://127.0.0.1.8000/ipltable
    path('model/', include("ModelWebApp.urls")),  # http://127.0.0.1.8000/model/getstudentdetails
    path('form/', include("FormWebApp.urls")),  # http://127.0.0.1.8000/form/register
    path('curd/', include("CURDApp.urls")),  # http://127.0.0.1.8000/curd/employeedetails
    path('alert/', include("AlertApp.urls")),  # http://127.0.0.1.8000/alert/show
    path('rest/', include("RestAPi.urls")),  # http://127.0.0.1.8000/rest/getuser

]
