from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('commande/', views.commande, name="commande"),
    path('appro/', views.appro, name="appro"),
    path('produit/', views.produit, name="produit"),
    path('produit/<str:pk>/', views.ficheProduit, name="fiche-produit"),
    path('create-produit/', views.createProduit, name="create-produit"),
    path('update-produit/<str:pk>/', views.updateProduit, name="update-produit"),
    path('delete-produit/<str:pk>', views.deleteProduit, name="delete-produit")
]
