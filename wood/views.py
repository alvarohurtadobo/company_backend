from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Wood_State
from .serializers import ProductSerializer, WoodStateSerializer
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
            "states": wood_state_serializer.data, 
            "locations": location_serializer.data})
