from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

def appro(request):
    return HttpResponse("Approvisionnement")

def commande(request):
    return HttpResponse("Commande")

def client(request):
    return HttpResponse("Client")

def stocks(request):
    return HttpResponse("Stocks")

def produit(request):
    return HttpResponse("Produits")
