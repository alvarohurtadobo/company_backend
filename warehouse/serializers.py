from rest_framework import serializers 
from . import models

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ["id", "name", "code", "country"] #"__all__"

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = ["id", "name", "city_id", "map_url"] #"__all__"

class LocationSerializer(serializers.ModelSerializer):
    warehouse_id = WarehouseSerializer()
    class Meta:
        model = models.Location
        fields = ["id", "name", 'warehouse_id'] #"__all__"

    def to_representation(self, instance):
        data = super(LocationSerializer, self).to_representation(instance)
        warehouse = data.pop('warehouse_id')
        for key, val in warehouse.items():
            if key=="id":
                data.update({"warehouse_id": val})
            if key=="city_id":
                data.update({"city_id": val})
        return data