from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=150, null=True, blank=True)
    TypeClient = models.TextChoices('TypeClient', 'PERSONNE ENTREPRISE')
    typeClient = models.CharField(
        blank=True, choices=TypeClient.choices, default='PERSONNE', max_length=12)
    email = models.CharField(max_length=100, unique=True)
    note = models.TextField(null=True, max_length=500, blank=True)
    pays = CountryField()
    ville = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if(self.prenom != None):
            return self.nom + " " + self.prenom
        return self.nom
