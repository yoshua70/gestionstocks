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
    produit = Produit.objects.get(designation=pk)
    context = { 'produit': produit }
    return render(request, 'base/ficheProduit.html', context)

def createProduit(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit')
    
    context = {'form': form}
    return render(request, 'base/produit_form.html', context)