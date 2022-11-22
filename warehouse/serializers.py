from rest_framework import serializers 
from . import models

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ["id", "name", "code", "country"] #"__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ["id", "name", "warehouse_id"] #"__all__"