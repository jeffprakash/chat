from django.shortcuts import render
from imaplib import _Authenticator
from xmlrpc.client import ResponseError
from django.shortcuts import render
from .serializers import infoserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets ,permissions
from django.contrib import auth
from .models import chat
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import infoserializer
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def get_list(request):                                         
    users=chat.objects.all()
    serializer =infoserializer(users, many=True)
    return Response(serializer.data)



class addinfo(APIView):
    def post(self, request):                                                
                                                                    

        serializer = infoserializer(data=request.data)
        if serializer.is_valid():
            # Create a new user
            # user = dataSerializer2.objects.create_user(
            #     username=serializer.data['name'],
            #     age=serializer.data['age'],                                   
            #     address=serializer.data['address'],
            #     email=serializer.data['email'],
            #     college=serializer.data['college'],
            #     password=serializer.data['password'],
            #     phno=serializer.data['phno'],
            #     location=serializer.data['location']
                
            # )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

