from rest_framework import serializers

from . import models


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
