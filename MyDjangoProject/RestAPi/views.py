from rest_framework.decorators import api_view
from rest_framework.response import Response
from RestAPi.models import UserRegister
from RestAPi.serializer import UserRegisterSerializer
@api_view(["GET"])
def getUser(request):
    user=UserRegister.objects.all()
    serializers=UserRegisterSerializer(user,many=True)
    return Response(serializers.data)
@api_view(["POST","GET"])
def createuser(request):
    newuser=UserRegisterSerializer(data=request.data)
    if newuser.is_valid():
        newuser.save()
    return Response(newuser.data)
