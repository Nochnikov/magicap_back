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
    facilities = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'facilities']

    def get_facilities(self, obj):
        facilities = obj.facility_set.all()[:3]
        return FacilitySerializer(facilities, many=True).data






