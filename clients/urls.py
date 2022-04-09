from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients, name="clients"),
    path('create-client/', views.createClient, name="create-client"),
    path('update-client/<str:pk>/', views.updateClient, name="update-client"),
    path('client/<str:pk>/', views.ficheClient, name="fiche-client"),
    path('delete-client/<str:pk>/', views.deleteClient, name="delete-client")
]
