from django.urls import path
from hr.views import *


urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('create_category/', CreateCategoryView.as_view(), name='create_category'),
    path('create_benefit/', CreateBenefitsView.as_view(), name='create_benefit'),


    path('users/', ListUsersView.as_view(), name='users'),
    path('categories/', ListCategoryView.as_view(), name='categories'),
    path('benefits/', ListBenefitsView.as_view(), name='benefits'),

    path('users/<int:pk>/', EditDeleteUserView.as_view(), name='users'),
    path('categories/<int:pk>/', EditDeleteCategoryView.as_view(), name='categories'),
    path('benefits/<int:pk>/', EditDeleteBenefitView.as_view(), name='benefits'),

    path('orders/', AllOrdersView.as_view(), name="orders"),
]