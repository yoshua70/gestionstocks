from django.db import models

# Create your models here.
class MatierePremiere(models.Model):
    statusChoices   = [
        ('ENSTOCK', 'En Stock'),
        ('RUPTURE', 'En rupture'),
    ]
    codeMatiere     = models.CharField(max_length=50, unique=True)
    libelleMatiere  = models.CharField(max_length=100)
    description     = models.TextField()
    status          = models.CharField(max_length=10, choices=statusChoices)
    updatedAt       = models.DateTimeField(auto_now=True)
    createdAt       = models.DateTimeField(auto_now_add=True)
