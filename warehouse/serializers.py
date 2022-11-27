from rest_framework import serializers
from . import models


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ["id", "name", "code", "country"]  # "__all__"


class WarehouseSerializer(serializers.ModelSerializer):
    city_id = CitySerializer()

    class Meta:
        model = models.Warehouse
        fields = ["id", "name", "city_id", "map_url"]  # "__all__"

    def to_representation(self, instance):
        data = super(WarehouseSerializer, self).to_representation(instance)
        city = data.pop("city_id")
        for key, val in city.items():
            if key == "id":
                data.update({"city_id": val})
            if key == "name":
                data.update({"city_name": val})
        return data


class LocationSerializer(serializers.ModelSerializer):
    warehouse_id = WarehouseSerializer()

    class Meta:
        model = models.Location
        fields = ["id", "name", 'warehouse_id']  # "__all__"

    def to_representation(self, instance):
        data = super(LocationSerializer, self).to_representation(instance)
        warehouse = data.pop('warehouse_id')
        for key, val in warehouse.items():
            if key == "id":
                data.update({"warehouse_id": val})
            if key == "name":
                data.update({"warehouse_name": val})
            if key == "city_id":
                data.update({"city_id": val})
        return data
