from django.shortcuts import render, redirect
from produits.forms import ProduitForm
from produits.models import Produit


def home(request):
    return render(request, 'produits/home.html')


def produit(request):
    produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'produits/produit.html', context)


def ficheProduit(request, pk):
    produit = Produit.objects.get(id=pk)
    context = {'produit': produit}
    return render(request, 'produits/fiche-produit.html', context)


def createProduit(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit')

    context = {'form': form, 'operation': "create"}
    return render(request, 'produits/produit_form.html', context)


def updateProduit(request, pk):
    produit = Produit.objects.get(id=pk)
    form = ProduitForm(instance=produit)

    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid:
            produit = form.save()
            return redirect('fiche-produit', pk=produit.id)

    context = {'form': form, 'operation': "update"}
    return render(request, 'produits/produit_form.html', context)


def deleteProduit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('produit')
    return render(request, 'produits/delete_produit.html', {'obj': produit})
