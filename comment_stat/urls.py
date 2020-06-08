from django.urls import path
from . import views

urlpatterns = [
    path('', views.stat),
    path('get_stat/', views.get_stat),
    path('get_region_stat/<int:region_id>/', views.get_region_stat),
]
