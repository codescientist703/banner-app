from django.urls import path

from . import views

urlpatterns = [
    path('banner/<pk>/', views.BannerView.as_view()),
]