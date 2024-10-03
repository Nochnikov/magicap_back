from rest_framework import serializers

from authorization.models import User


class CreateUpdateDeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'first_name', 'last_name', 'gender',
                  'avatar', 'country', 'phone_number', 'coins']
