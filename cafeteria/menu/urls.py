from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('pedido/', views.pedido, name='pedido'),
    path('buscar/', views.buscar, name='buscar'),
]