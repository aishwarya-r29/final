from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('factory/dashboard/', views.factory_dashboard, name='factory_dashboard'),
    path('upload_batch/', views.upload_batch, name='upload_batch'),
    path('post_demand/', views.post_demand, name='post_demand'),
    path('matches/', views.matches, name='matches'),
]
