from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('about/', views.about),
    path('chat/', views.chat),
    path('food/', views.FoodList.as_view()),
    
]