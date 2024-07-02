from django.urls import path
from facility import views



urlpatterns = [
    path('main/', views.CategoriesWithFacilitiesView.as_view(), name='main'),
    path('main/<int:category_id>/', views.FacilityListByCategoryView.as_view(), name='facility-list'),
    path('main/facility_detail/<int:pk>/', views.FacilityDetailView.as_view(), name='facility-detail'),

    path('main/facalities/', views.CategoriesWithCountView.as_view(), name='facility-count'),
    path('main/facility/<int:facility_id>/', views.OrderFacilitiesView.as_view(), name='facility-order'),

    # #admin only
    # #удалить
    path('main/create/', views.FacilityCreateView.as_view(), name='facility-create'),
    path('main/categories/', views.CategoryCreateListView.as_view(), name='facility-list'),
    path('main/categories/<int:pk>', views.CategoryDetailUpdateView.as_view(), name='facility-detail-refactoring'),

]