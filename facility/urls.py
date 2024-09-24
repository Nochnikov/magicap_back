from django.urls import path
from facility import views



urlpatterns = [
    path('', views.CategoriesWithCountView.as_view(), name='benefit-count'),
    path('top/', views.CategoriesWithBenefitsView.as_view(), name='top'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('<int:category_id>/', views.BenefitsListByCategoryView.as_view(), name='benefit-list'),
    path('detail/<int:pk>/', views.BenefitDetailView.as_view(), name='benefit-detail'),
    path('order/<int:benefit_id>/', views.OrderBenefitsView.as_view(), name='benefit-order'),

]



