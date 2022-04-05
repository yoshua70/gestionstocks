from django.urls import path
from . import views

urlpatterns = [
    path('', views.produit, name="produit"),
    path('produit/<str:pk>/', views.ficheProduit, name="fiche-produit"),
    path('create-produit/', views.createProduit, name="create-produit"),
    path('update-produit/<str:pk>/', views.updateProduit, name="update-produit"),
    path('delete-produit/<str:pk>', views.deleteProduit, name="delete-produit")
]
