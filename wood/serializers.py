from rest_framework import serializers

from . import models
from warehouse.models import Location
from warehouse.serializers import LocationSerializer


class LineSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Line
        fields = ["id", "name"]  # "__all__"


class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["id", "name", "code", "inventory_type_id",
                    "line_id", "is_wood", "length", "width",
                    "height", "species", "created_at", "updated_at"]  # "__all__"


class WoodStateSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Wood_State
        fields = ["id", "name"]

class KitSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Kit
        fields = '__all__'

class ExtendedKitSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()
    location_id = LocationSerializer()
    state_id = WoodStateSerializer()
    class Meta:
        model = models.Kit
        fields = "__all__"

    def to_representation(self, instance):
        data = super(ExtendedKitSerializer, self).to_representation(instance)
        product = data.pop('product_id')
        for key, val in product.items():
            if key=="id":
                data.update({"product_id": val})
            if key=="name":
                data.update({"product_name": val})
            if key=="code":
                data.update({"product_code": val})
            if key=="is_wood":
                data.update({"product_is_wood": val})
            if key=="height":
                data.update({"product_height": val})
            if key=="width":
                data.update({"product_width": val})
            if key=="length":
                data.update({"product_length": val})
            
        location = data.pop('location_id')
        for key, val in location.items():
            if key=="id":
                data.update({"location_id": val})
            if key=="city_id":
                data.update({"city_id": val})
            if key=="name":
                data.update({"location_name": val})
            if key=="warehouse_name":
                data.update({"warehouse_name": val})

        status = data.pop('state_id')
        for key, val in status.items():
            if key=="id":
                data.update({"state_id": val})
            if key=="name":
                data.update({"wood_state_name": val})
        return data