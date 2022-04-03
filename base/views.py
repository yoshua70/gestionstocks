from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def appro(request):
    return render(request, 'appro.html')

def commande(request):
    return HttpResponse("Commande")

def client(request):
    return HttpResponse("Client")

def stocks(request):
    return HttpResponse("Stocks")

def produit(request):
    return render(request, 'produit.html')
