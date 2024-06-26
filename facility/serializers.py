from rest_framework import serializers
from facility.models import Facility, Category

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryMainPageSerializer(CategorySerializer):
    facilities = FacilitySerializer(many=True, read_only=True)


    class Meta:
        model = Category
        fields = ['name', 'facilities']






