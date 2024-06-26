from django.urls import path
from facility import views



urlpatterns = [
    path('main/<int: category_id>', views.FacilityListByCategoryView.as_view(), name='facility-list'),
    path('main/<int:pk>/', views.FacilityDetailView.as_view(), name='facility-detail'),


    #admin only
    path('main/create/', views.FacilityCreateView.as_view(), name='facility-create'),

]