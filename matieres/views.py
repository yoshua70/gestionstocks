from django.shortcuts import render

from matieres.models import MatierePremiere

# Create your views here.


def matiere(request):
    listeMatiere = MatierePremiere.objects.all()
    context = {
        'matierePremiere': listeMatiere
    }
    return render(request, 'matieres/matiere.html', context)
