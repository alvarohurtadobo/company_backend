from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Product, Wood_State, Kit
from .serializers import ProductSerializer, WoodStateSerializer, KitSerializer
from warehouse.models import Location
from warehouse.serializers import LocationSerializer


@api_view(['GET'])
def get_settings(request, format=None):
    if request.method == 'GET':
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        wood_states = Wood_State.objects.all()
        wood_state_serializer = WoodStateSerializer(wood_states, many=True)
        locations = Location.objects.all()
        location_serializer = LocationSerializer(locations, many=True)
        # Para listas , safe= False
        return Response({"products": product_serializer.data, 
            "wood_states": wood_state_serializer.data, 
            "locations": location_serializer.data})
    
@api_view(['GET', 'POST'])
def listOrCreateKit(request, format=None):
    if request.method == 'GET':
        kits = Kit.objects.all()
        kit_serializer = KitSerializer(kits, many=True)
        return Response({"kits":kit_serializer.data})
    if request.method == 'POST':
        kit_serializer = KitSerializer(data=request.data)
        if kit_serializer.is_valid():
            kit_serializer.save()
            return Response(kit_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(kit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT', 'DELETE'])
def readUpdateOrDelete(request, kit_id, format=None):
    try:
        kit = Kit.objects.get(pk=kit_id)
    except Kit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        kit_serializer = KitSerializer(kit)
        return Response({"kit":kit_serializer.data})
    if request.method == 'PUT':
        kit_serializer = KitSerializer(kit,many=False,data=request.data)
        if kit_serializer.is_valid():
            kit_serializer.save()
            return Response(kit_serializer.data)
        else:
            return Response(kit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        kit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)