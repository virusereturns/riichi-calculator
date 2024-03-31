from django.urls import path
from . import views

urlpatterns = [
    path('api/calculate/', views.ScoreCalcAPI.as_view(), name='calculate_api'),
    path('calculate/', views.ScoreCalcHTMXView.as_view(), name='calculate_view'),
    path('', views.ScoreCalcView.as_view(), name='home'),
]
