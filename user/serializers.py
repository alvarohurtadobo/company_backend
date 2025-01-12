from rest_framework import serializers 
from . import models

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = ["id", "name"] #"__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','email','password','first_name', 'last_name', 'active', 'city_id', 'role_id')
        extra_kwargs = {
            'password':{'write_only': True},
        }

        def create(self, validated_data):
            user = models.User.objects.create_user( validated_data['email'],
                                                    password = validated_data['password'],
                                                    first_name=validated_data['first_name'],  
                                                    last_name=validated_data['last_name'])
            return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = '__all__'