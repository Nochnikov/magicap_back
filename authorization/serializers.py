from rest_framework import serializers
from authorization.models import User
from facility.serializers import OrderSerializer


class MyProfileSerializer(serializers.ModelSerializer):

    orders = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'date_of_birth', 'country', 'avatar', 'email', 'gender', 'coins', 'role',
                  'orders', 'phone_number']
        read_only_fields = ['coins', 'role', 'orders',]
