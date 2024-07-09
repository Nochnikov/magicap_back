from django.urls import path
from facility import views



urlpatterns = [
    path('main/', views.CategoriesWithFacilitiesView.as_view(), name='main'),
    path('main/<int:category_id>/', views.BenefitsListByCategoryView.as_view(), name='facility-list'),
    path('main/benefit_detail/<int:pk>/', views.BenefitDetailView.as_view(), name='facility-detail'),

    path('main/benefits/', views.CategoriesWithCountView.as_view(), name='facility-count'),
    path('main/benefit/<int:benefit_id>/', views.OrderFacilitiesView.as_view(), name='facility-order'),

]