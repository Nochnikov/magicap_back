from rest_framework import serializers
from authorization.models import User
from facility.serializers import OrderSerializer


class MyProfileSerializer(serializers.ModelSerializer):

    orders = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'coins', 'role', 'orders']
        read_only_fields = ['coins', 'role', 'orders']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




