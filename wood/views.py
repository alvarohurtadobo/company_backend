from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Product, Wood_State, Kit, Line
from .serializers import ExtendedKitSerializer, UltimateKitSerializer, ProductSerializer, WoodStateSerializer, KitSerializer, LineSerializer
from warehouse.models import Location, City
from warehouse.serializers import LocationSerializer

@api_view(['GET'])
def list_products_by_city(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    products = city.products.all()
    product_serializer = ProductSerializer(products, many=True)
    return Response({"products":product_serializer.data})

@api_view(['GET'])
def get_settings(request, format=None):
    if request.method == 'GET':
        lines = Line.objects.all()
        line_serializer = LineSerializer(lines, many=True)
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        wood_states = Wood_State.objects.all()
        wood_state_serializer = WoodStateSerializer(wood_states, many=True)
        locations = Location.objects.all()
        location_serializer = LocationSerializer(locations, many=True)
        # Para listas , safe= False
        return Response({
                "lines":line_serializer.data,
                "products": product_serializer.data, 
                "wood_states": wood_state_serializer.data, 
                "locations": location_serializer.data
            })
    
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
        
@api_view(['POST'])
def searchKits(request, format=None):
    kits = Kit.objects.all()
    if "product_id" in request.data:
        product_id = request.data["product_id"]
        kits = kits.filter(product_id=product_id) 
    if "state_id" in request.data:
        state_id = request.data["state_id"]
        kits = kits.filter(state_id=state_id) 
    if "location_id" in request.data:
        location_id = request.data["location_id"]
        kits = kits.filter(location_id=location_id) 
    if "city_id" in request.data:
        city_id = request.data["city_id"]
        kits = kits.filter(location_id__warehouse_id__city_id=city_id) 
    if "amount_min" in request.data:
        amount_min = request.data["amount_min"]
        kits = kits.filter(amount__gte=amount_min) 
    # Equal
    if "length" in request.data:
        length = request.data["length"]
        kits = kits.filter(product_id__length=length) 
    if "width" in request.data:
        width = request.data["width"]
        kits = kits.filter(product_id__width=width) 
    if "height" in request.data:
        height = request.data["height"]
        kits = kits.filter(product_id__height=height) 
    # Greater than
    if "length_min" in request.data:
        length_min = request.data["length_min"]
        kits = kits.filter(product_id__length__gte=length_min) 
    if "width_min" in request.data:
        width_min = request.data["width_min"]
        kits = kits.filter(product_id__width__gte=width_min) 
    if "height_min" in request.data:
        height_min = request.data["height_min"]
        kits = kits.filter(product_id__height__gte=height_min)
    # Less than than
    if "length_max" in request.data:
        length_max = request.data["length_max"]
        kits = kits.filter(product_id__length__lte=length_max) 
    if "width_max" in request.data:
        width_max = request.data["width_max"]
        kits = kits.filter(product_id__width__lte=width_max) 
    if "height_max" in request.data:
        height_max = request.data["height_max"]
        kits = kits.filter(product_id__height__lte=height_max)  
    kits = kits.order_by("-created_at")
    kit_serializer = ExtendedKitSerializer(kits, many=True)
    return Response({"kits":kit_serializer.data})

@api_view(["GET"])
def read_kit_expanded(request, kit_id):
    kit = get_object_or_404(Kit, pk=kit_id)
    kit_serializer = UltimateKitSerializer(kit, many=False);
    return Response({"kit":kit_serializer.data})

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