from django.db import models

# Create your models here.


class Stocks(models.Model):
    designation = models.CharField(max_length=50)
    quantité = models.FloatField()
    unité = models.CharField(max_length=50)
    type = models.TextChoices('TypeStock', 'PRODUIT MATIERES')
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.designation
