from django.shortcuts import render

# Create your views here.


def commandes(request):
    context = {}
    return render(request, 'commandes/commandes.html', context)
