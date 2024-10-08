from rest_framework import generics
from rest_framework.response import Response

from facility.models import Benefit, Category, Order
from facility.serializers import BenefitSerializer, CategoryMainPageSerializer, \
    CategoryWithCountSerializer, CategorySerializer


# Create your views here.


# class CategoriesWithCountView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryWithCountSerializer

class CategoriesWithCountView(generics.ListAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

class CategoriesWithBenefitsView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryMainPageSerializer

    def get_queryset(self):
        qs = Category.objects.all()[:3]
        return qs

class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BenefitsListByCategoryView(generics.ListAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')

        qs = Benefit.objects.all().filter(category=category_id)
        return qs


class BenefitDetailView(generics.RetrieveAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer


class OrderBenefitsView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        benefit_id = self.kwargs.get('benefit_id')
        user = self.request.user

        try:
            cost = Benefit.objects.all().get(pk=benefit_id).cost
        except Exception:
            raise {"message": f"Benefit with ID {benefit_id} does not exist"}


        if user.coins < cost:
            return Response({"msg": "Not enough coins"})

        user.coins -= cost
        user.save()


        order = Order.objects.create(user=user)
        order.benefits.add(benefit_id)
        order.save()

        return Response({"msg": "Benefit added to a database"})