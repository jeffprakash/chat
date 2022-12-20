from rest_framework import serializers
from .models import chat

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= User
#         fields= ['id','username','password','email']


class infoserializer(serializers.ModelSerializer):
    class Meta:
        model= chat
        fields= ['info1','info2']