from django.urls import path
from facility import views



urlpatterns = [
    path('main/', views.CategoriesWithFacilitiesView.as_view(), name='main'),
    path('main/<int:category_id>/', views.FacilityListByCategoryView.as_view(), name='facility-list'),
    path('main/<int:pk>/', views.FacilityDetailView.as_view(), name='facility-detail'),


    #admin only
    path('main/create/', views.FacilityCreateView.as_view(), name='facility-create'),
    path('main/categories/', views.CategoryCreateListView.as_view(), name='facility-list'),
    path('main/categories/<int:pk>', views.CategoryDetailUpdateView.as_view(), name='facility-detail-refactoring'),

]