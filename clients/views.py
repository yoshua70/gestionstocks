from django.shortcuts import render

# Create your views here.


def clients(request):
    context = {}
    return render(request, 'clients/clients.html', context)
