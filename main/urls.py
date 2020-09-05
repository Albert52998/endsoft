from django.urls import path

from . import views

urlpatterns = [
    path('soft/<int:soft_id>/', views.by_soft, name='by_soft'),
    path('category/<int:category_id>/', views.by_category, name='by_category'),
    path('soft/download/<int:soft_id>/', views.soft_downloads_count, name='soft_downloads_count'),
    path('', views.index, name='home')
]