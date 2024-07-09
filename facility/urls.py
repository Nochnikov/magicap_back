from django.urls import path
from facility import views



urlpatterns = [
    path('main/', views.CategoriesWithFacilitiesView.as_view(), name='main'),
    path('main/<int:category_id>/', views.BenefitsListByCategoryView.as_view(), name='facility-list'),
    path('main/facility_detail/<int:pk>/', views.BenefitDetailView.as_view(), name='facility-detail'),

    path('main/facalities/', views.CategoriesWithCountView.as_view(), name='facility-count'),
    path('main/facility/<int:facility_id>/', views.OrderFacilitiesView.as_view(), name='facility-order'),

]