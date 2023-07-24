from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categoria/', views.categoria, name='categoria'),
]