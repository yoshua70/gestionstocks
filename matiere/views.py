from django.shortcuts import render
from .models import MatierePremiere

# Create your views here.
def matiere(request):
    listeMatiere = MatierePremiere.objects.all()
    context = {
        'matierePremiere':listeMatiere
    }
    return render(request,'base/matiere.html', context)

def createMatiere(request):
    pass

def ficheMatiere(request):
    pass

def updateMatiere(request):
    pass 

def deleteMatiere(request):
    pass
