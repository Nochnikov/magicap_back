from rest_framework import generics, permissions
from facility.models import Facility, Category
from facility.serializers import FacilitySerializer, CategorySerializer, CategoryMainPageSerializer

# Create your views here.

class CategoriesWithFacilitiesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryMainPageSerializer
    """
        have to check
    """



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

class CategoryCreateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'






