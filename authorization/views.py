from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from authorization.models import User
from authorization.serializers import MyProfileSerializer


# Create your views here.


class ProfileRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = MyProfileSerializer


    def get_object(self):
        user = User.objects.prefetch_related(
            'orders__benefits'
        ).get(pk=self.request.user.pk)
        return user
