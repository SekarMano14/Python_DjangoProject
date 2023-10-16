from rest_framework import serializers

from RestAPi.models import UserRegister


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRegister
        fields="__all__"