from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializer import UserCreationSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class UserCreationView(generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserCreationSerializer

    @swagger_auto_schema(operation_summary="Create User Account")
    def post(self, request, *args, **kwargs):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)           
       


