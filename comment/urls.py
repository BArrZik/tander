from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment),
    path('get_city_by_region_id/<int:region_id>/', views.get_city_by_region_id),
]


