from django.db import models

# Create your models here.

class Produit(models.Model):
    designation = models.CharField(max_length=50, unique=True)
    libelle = models.CharField(max_length=100)
    description = models.TextField(null=True, max_length=500, blank=True)
    StatutStock = models.TextChoices('StatutStock', 'ENSTOCK RUPTURE')
    statut = models.CharField(blank=True, choices=StatutStock.choices, default='ENSTOCK', max_length=10)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.designation

class Stocks(models.Model):
    designation = models.CharField(max_length=50)
    quantité = models.FloatField()
    unité = models.CharField(max_length=50)
    type = models.TextChoices('TypeStock', 'PRODUIT MATIERES')
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.designation
