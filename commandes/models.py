import uuid
from django.db import models

from clients.models import Client
from produits.models import Produit

# Create your models here.


class Commande(models.Model):
    numero = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    StatutCommande = models.TextChoices(
        'StatutCommande', 'REÇU ENCOURS COMPLETE')
    statut = models.CharField(
        blank=True, choices=StatutCommande.choices, default='REÇU', max_length=10)


class CommandeProduit(models.Model):
    idCommande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    idProduit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.BigIntegerField()
