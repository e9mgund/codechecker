from django.urls import path
from apps.codechecker import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home')
]