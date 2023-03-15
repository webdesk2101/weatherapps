from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/', views.api_view, name='api')
]
