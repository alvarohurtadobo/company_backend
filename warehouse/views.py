from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Warehouse
from .serializers import WarehouseSerializer


@api_view(["GET"])
def listWarehouses(request):
    warehouses = Warehouse.objects.all()
    warehouse_serializer = WarehouseSerializer(warehouses, many=True)
    return Response({"warehouses": warehouse_serializer.data})
