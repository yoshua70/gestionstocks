from django.shortcuts import render
from django.http import HttpResponse

produits = [
        {'libelle': 'Sneakers', 'designation': 'snk001', 'description': 'Des sneakers solides pour vous accompagner dans tous vos déplacements', 'statut': 'en stock'},
        {'libelle': 'T-shirt Sportif', 'designation': 'tshirtsport', 'description': 'Du coton de qualité pour vos activités sportives', 'statut': 'en stock'},
        {'libelle': 'Montre Tactique GX-0', 'designation': 'gx0', 'description': "Montre tactique, résistante à l'eau", 'statut': 'en stock'},
    ]

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
    context = { 'produits': produits }
    return render(request, 'base/produit.html', context)

def ficheProduit(request, pk):
    for i in produits: 
        if i['designation'] == pk:
            produit = i
    context = { 'produit': produit }
    return render(request, 'base/ficheProduit.html', context)
