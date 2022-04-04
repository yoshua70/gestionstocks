from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.forms import ProduitForm
from base.models import Produit

def home(request):
    return render(request, 'base/home.html')

def appro(request):
    return render(request, 'base/appro.html')

def commande(request):
    return HttpResponse("Commande")

def client(request):
    return HttpResponse("Client")

def stocks(request):
    return HttpResponse("Stocks")

def produit(request):
    produits = Produit.objects.all()
    context = { 'produits': produits }
    return render(request, 'base/produit.html', context)

def ficheProduit(request, pk):
    produit = Produit.objects.get(id=pk)
    context = { 'produit': produit }
    return render(request, 'base/ficheProduit.html', context)

def createProduit(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit')
    
    context = {'form': form, 'operation': "create"}
    return render(request, 'base/produit_form.html', context)

def updateProduit(request, pk):
    produit = Produit.objects.get(id=pk)
    form = ProduitForm(instance=produit)

    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid:
            produit = form.save()
            return redirect('fiche-produit', pk=produit.id)

    context = {'form': form, 'operation': "update"}
    return render(request, 'base/produit_form.html', context)

def deleteProduit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('produit')
    return render(request, 'base/delete_produit.html', {'obj': produit})
