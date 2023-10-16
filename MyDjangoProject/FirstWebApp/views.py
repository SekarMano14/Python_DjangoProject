from django.http import HttpResponse


# Create your views here.
# def homepage(request):
#     home = """<html>
# <head>
# <title>This My Django Application</title>
# </head>
# <body>
# <h1>Hai This My First Django Web Application</h1>
# <h2>welcome To All</h2>
#  <h2 style='color:blue;text-align:center'>Enter to the app <a href='/login'>login here</a></h2>
#   <h2 style='color:green;text-align:center'>If Your are new ..<a href='/register'>register here</a></h2>
#  </body>
# </html>
# """
#     return HttpResponse(home)
#
# def loginpage(request):
#     login = """<html>
#     <head>
#     <title>My DjangoApp| Login</title>
#     </head>
#     <body>
#     <h1>Welcome To User</h1>
#     <input type='text' placeholder="enter the username"/>
#     <input type='text' placeholder="enter the password"/>
#     <input type='submit' value="Login"/>
#     </body>
#     </html>
#     """
#     return HttpResponse(login)
#
# def registerpage(request):
#     reg = """<html>
#     <head>
#     <title>My DjangoApp| Register</title>
#     </head>
#     <body>
#     <h1>Welcome To My app</h1>
#     <p>Enter the Firstname, lastname and phno. etc..</p>
#      <input type='text' placeholder="enter the Firstname"/>
#     <input type='text' placeholder="enter the MobileNumber"/>
#     <input type='submit' value="Submit"/>
#     </body>
#     </html>
#     """
#     return HttpResponse(reg)
from django.shortcuts import render


def homepage(request):
    return render(request,"Firstwebapp\home.html")

def loginpage(request):
    return render(request,"Firstwebapp\login.html")

def registerpage(request):
    return render(request,"Firstwebapp\\register.html")


