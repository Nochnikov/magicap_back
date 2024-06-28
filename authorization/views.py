from django.shortcuts import render
from rest_framework import generics
from authorization.models import User
from authorization.serializers import MyProfileSerializer, UserProfileSerializer, UserSerializer


# Create your views here.


class ProfileRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = MyProfileSerializer

    def get_object(self):
        instance = User.objects.get(id=self.request.user.id)
        return instance

"""

below will be view for admin only 
"""

class ProfileListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'











