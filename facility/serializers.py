from rest_framework import serializers
from facility.models import Benefit, Category, Order


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'


class CategoryWithCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'count']

    def get_count(self, obj):
        count = obj.benefit_set.count()
        return count

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryMainPageSerializer(CategorySerializer):
    benefits = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'benefits']

    def get_benefits(self, obj):
        benefits = obj.benefit_set.all()[:3]
        return BenefitSerializer(benefits, many=True).data

class OrderSerializer(serializers.ModelSerializer):

    benefits = BenefitSerializer(read_only=False, many=True)

    class Meta:
        model = Order
        fields = ['date', 'benefits']