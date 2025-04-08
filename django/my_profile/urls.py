from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfile.as_view(), name='profile'),

]