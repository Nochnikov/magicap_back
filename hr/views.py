from django.contrib.auth.hashers import make_password
from rest_framework import generics, mixins

from authorization.models import User
from facility.models import Category, Benefit
from facility.serializers import CategorySerializer, BenefitSerializer
from hr.serializers import *
from hr.permissions import *

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUpdateDeleteUserSerializer
    permission_classes = (IsHRorAdmin,)

class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUpdateDeleteUserSerializer

class EditDeleteUserView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = CreateUpdateDeleteUserSerializer

    permission_classes = (IsHRorAdmin,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):

        password = request.data.get('password')
        password = make_password(password)
        request.data['password'] = password

        return self.partial_update(request, *args, **kwargs)


class CreateCategoryView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsHRorAdmin,)
class ListCategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EditDeleteCategoryView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                             mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsHRorAdmin,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CreateBenefitsView(generics.CreateAPIView):
    serializer_class = BenefitSerializer
    permission_classes = (IsHRorAdmin,)

class ListBenefitsView(generics.ListAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

class EditDeleteBenefitView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
    permission_classes = (IsHRorAdmin,)


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


