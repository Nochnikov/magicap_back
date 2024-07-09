from rest_framework import generics
from rest_framework.response import Response

from facility.models import Benefit, Category, Order
from facility.serializers import FacilitySerializer, CategoryMainPageSerializer, \
    CategoryWithCountSerializer, OrderSerializer


# Create your views here.


class CategoriesWithCountView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithCountSerializer


class CategoriesWithFacilitiesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryMainPageSerializer

    def get_queryset(self):
        qs = Category.objects.all()[:3]
        return qs


class BenefitsListByCategoryView(generics.ListAPIView):
    queryset = Benefit.objects.all()
    serializer_class = FacilitySerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')

        qs = Benefit.objects.all().filter(category=category_id)
        return qs


class BenefitDetailView(generics.RetrieveAPIView):
    queryset = Benefit.objects.all()
    serializer_class = FacilitySerializer


class OrderFacilitiesView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        benefit_id = self.kwargs.get('benefit_id')
        user = self.request.user

        try:
            cost = Benefit.objects.all().get(pk=benefit_id).cost
        except Exception:
            raise {"message": f"Facility with ID {benefit_id} does not exist"}


        if user.coins < cost:
            return Response({"msg": "Not enough money"})

        user.coins -= cost
        user.save()


        order = Order.objects.create(user=user)
        order.facilities.add(benefit_id)
        order.save()

        return Response({"msg": "Facility added to database"})