from django.urls import path
from rest_framework_simplejwt import views as rest_framework
from authorization.views import ProfileRetrieveUpdateView


urlpatterns = [
    path('login/', rest_framework.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', rest_framework.TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', ProfileRetrieveUpdateView.as_view(), name='profile')

]
