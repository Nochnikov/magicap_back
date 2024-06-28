from django.urls import path
from rest_framework_simplejwt import views as rest_framework
from authorization.views import ProfileRetrieveUpdateView, ProfileListView, ProfileRetrieveUpdateDeleteView


urlpatterns = [
    path('login/', rest_framework.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', rest_framework.TokenRefreshView.as_view(), name='token_refresh'),

    path('my-profile/', ProfileRetrieveUpdateView.as_view(), name='my_profile'),

    """
        admin only urls
    """,

    path('users/list/', ProfileListView.as_view(), name='users_list' ),
    path('users/<int:pk>/', ProfileRetrieveUpdateDeleteView.as_view(), name='user_profile' )

]