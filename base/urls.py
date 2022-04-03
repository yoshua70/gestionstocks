from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('commande/', views.commande, name="commande"),
    path('appro/', views.appro, name="appro"),
    path('produit/', views.produit, name="produit")
]
