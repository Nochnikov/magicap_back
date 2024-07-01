from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response

from facility.models import Facility, Category, Order
from facility.serializers import FacilitySerializer, CategorySerializer, CategoryMainPageSerializer, \
    CategoryWithCountSerializer, OrderSerializer


# Create your views here.


class CategoriesWithCountView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithCountSerializer


class CategoriesWithFacilitiesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryMainPageSerializer


class FacilityListByCategoryView(generics.ListAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')

        qs = Facility.objects.all().filter(category=category_id)
        return qs


class FacilityDetailView(generics.RetrieveAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


"""

Below admin only views

"""


class FacilityCreateView(generics.CreateAPIView):
    # permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class FacilityUpdateView(generics.UpdateAPIView):
    # permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


class OrderFacilitiesView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        facility_id = self.kwargs.get('facility_id')
        user = self.request.user

        try:
            cost = Facility.objects.all().get(pk=facility_id).cost
        except Exception:
            raise {"message": f"Facility with ID {facility_id} does not exist"}


        if user.coins < cost:
            return Response({"msg": "Not enough money"})

        user.coins -= cost
        user.save()


        order = Order.objects.create(user=user)
        order.facilities.add(facility_id)
        order.save()
