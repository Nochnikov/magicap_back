from rest_framework import generics, permissions
from authorization.models import User
from authorization.serializers import MyProfileSerializer, UserProfileSerializer, UserSerializer


# Create your views here.


class ProfileRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):

    # permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = MyProfileSerializer


    def get_object(self):
        user = User.objects.prefetch_related(
            'orders__facilities'
        ).get(pk=self.request.user.pk)
        return user
