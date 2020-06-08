from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.view),
    path('get_comments/', views.get_comments),
    path('delete_row/<int:id>', views.delete_row),
    path('get_regions/', include('comment.urls')),
]
