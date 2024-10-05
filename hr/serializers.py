from rest_framework import serializers

from authorization.models import User
from facility.serializers import OrderSerializer


class CreateUpdateDeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'gender',
                  'avatar', 'country', 'phone_number', 'coins', 'company']



class UserOrdersSerializer(serializers.ModelSerializer):


    orders = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'gender',
                  'avatar', 'country', 'phone_number', 'coins', 'company', 'orders']
