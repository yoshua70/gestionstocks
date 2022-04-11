from django.shortcuts import redirect, render

from commandes.forms import CommandeForm
from produits.models import Produit

# Create your views here.


def commandes(request):
    context = {}
    return render(request, 'commandes/commandes.html', context)


def createCommande(request):
    form = CommandeForm
    produits = Produit.objects.all()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    context = {'form': form, 'operation': "create", 'produits': produits}
    return render(request, 'commandes/commande_form.html', context)
