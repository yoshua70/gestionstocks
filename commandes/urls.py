from django.urls import path
from . import views

urlpatterns = [
    path('', views.commandes, name="commandes"),
    path('create-commande/', views.createCommande, name="create-commande")
]
