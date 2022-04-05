from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from matieres.models import MatierePremiere
from .forms import MatierePremiereForm

# Create your views here.


def matiere(request):
    listeMatiere = MatierePremiere.objects.all()
    context = {
        'matierePremiere': listeMatiere
    }
    return render(request, 'matieres/matiere.html', context)

def createMatiere(request):
    form = MatierePremiereForm()
    if request.method == 'POST':
        form = MatierePremiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matieres')

    context = {'form': form, 'operation': "create"}
    return render(request, 'matieres/matiere_form.html', context)

def updateMatiere(request,pk):
    instance = get_object_or_404(MatierePremiere, id=pk)
    form = MatierePremiereForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('matieres')
    return render(request, 'matieres/matiere_form.html', {'form':form, 'operation':'update'})

def deleteMatiere(request, pk):
    instance = get_object_or_404(MatierePremiere,id=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('matieres')
    return HttpResponse({'m':'message'})
    