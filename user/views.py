import json
from django import forms

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import make_password

from . import models
from . import serializers
from warehouse.models import City
from warehouse.serializers import CitySerializer
from wood.models import Line 
from wood.serializers import LineSerializer

class RoleView(viewsets.ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer

@api_view(['GET', 'POST'])
def role_list(request, format=None):
    if request.method == 'GET':
        roles = models.Role.objects.all()
        serializer = serializers.RoleSerializer(roles, many = True)
        return Response({"roles":serializer.data})  # Para listas , safe= False


    if request.method == 'POST':
        serializer = serializers.RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(["GET"])
def listEmployees(request):
    if request.method=='GET':
        employees = models.Employee.objects.all()
        serializer = serializers.EmployeeSerializer(employees, many = True)
        return Response({"employees":serializer.data})
    
@api_view(["GET"])
def listProviders(request):
    if request.method=='GET':
        providers = models.Provider.objects.all()
        serializer = serializers.ProviderSerializer(providers, many = True)
        return Response({"providers":serializer.data})

@api_view(['GET', 'PUT', 'DELETE'])
def role_update(request, role_id, format=None):
    try:
        role = models.Role.objects.get(pk=role_id)
    except models.Role.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer = serializers.RoleSerializer(role, many=False)
        return Response({"role":serializer.data})
    if request.method=="PUT":
        serializer = serializers.RoleSerializer(role, many=False, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
    reqBody = json.loads(request.body)
    email = reqBody["email"]
    password= reqBody["password"]
    print(f"Login user {email} with pasword {password}")
    try:
        user =  models.User.objects.get(email=email)
    except BaseException as e:
        print(f"Error triggers here {e}")
        return Response(status=status.HTTP_404_NOT_FOUND)
    if user.password == password:
        myRole = user.role_id
        myCity = user.city_id
        myCities = City.objects.all()
        myLines = Line.objects.all()
        return Response({
                "user": serializers.UserSerializer(user).data, 
                "role": serializers.RoleSerializer(myRole).data,
                "city": CitySerializer(myCity).data,
                "cities": CitySerializer(myCities, many=True).data,
                "lines": LineSerializer(myLines, many=True).data,
                "token": email})

@api_view(['POST'])
def loginNoPassword(request):
    reqBody = json.loads(request.body)
    email = reqBody["email"]
    print(f"Login user {email} NO PASSWORD")
    try:
        user =  models.User.objects.get(email=email)
    except BaseException as e:
        print(f"Error triggers here {e}")
        return Response(status=status.HTTP_404_NOT_FOUND)
    myRole = user.role_id
    myCity = user.city_id
    myCities = City.objects.all()
    myLines = Line.objects.all()
    return Response({
            "user": serializers.UserSerializer(user).data, 
            "role": serializers.RoleSerializer(myRole).data,
            "city": CitySerializer(myCity).data,
            "cities": CitySerializer(myCities, many=True).data,
            "lines": LineSerializer(myLines, many=True).data,
            "token":email})


class RegisterApi(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(f"User is {user}")
        return Response({
            "user": serializers.UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })