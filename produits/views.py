from django.shortcuts import render, redirect
<<<<<<< HEAD:base/views.py
from django.http import HttpResponse
from base.forms import ProduitForm
from base.models import Produit
=======
from produits.forms import ProduitForm
from produits.models import Produit

>>>>>>> de8943b1c6d5980c8aeae62bacd6828142451c5b:produits/views.py

def home(request):
    return render(request, 'produits/home.html')

<<<<<<< HEAD:base/views.py
def appro(request):
    return render(request, 'base/appro.html')

def commande(request):
    return HttpResponse("Commande")

def client(request):
    return HttpResponse("Client")

def stocks(request):
    return HttpResponse("Stocks")
=======
>>>>>>> de8943b1c6d5980c8aeae62bacd6828142451c5b:produits/views.py

def produit(request):
    produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'produits/produit.html', context)


def ficheProduit(request, pk):
    produit = Produit.objects.get(id=pk)
    context = {'produit': produit}
    return render(request, 'produits/ficheProduit.html', context)


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
