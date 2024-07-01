from rest_framework import serializers
from facility.models import Facility, Category, Order


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class CategoryWithCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'count']

    def get_count(self, obj):
        count = obj.facility_set.count()
        return count

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryMainPageSerializer(CategorySerializer):
    facilities = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'facilities']

    def get_facilities(self, obj):
        facilities = obj.facility_set.all()[:3]
        return FacilitySerializer(facilities, many=True).data

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



