from .models import Client
from django.shortcuts import redirect, render

from clients.forms import ClientForm

# Create your views here.


def clients(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'clients/clients.html', context)


def ficheClient(request, pk):
    client = Client.objects.get(id=pk)
    context = {'client': client}
    return render(request, 'clients/fiche_client.html', context)


def createClient(request):
    form = ClientForm
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    context = {'form': form, 'operation': "create"}
    return render(request, 'clients/client_form.html', context)


def updateClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid:
            client = form.save()
            return redirect('fiche-client', pk=client.pk)

    context = {'form': form, 'operation': "update"}
    return render(request, 'clients/client_form.html', context)


def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients')
    return render(request, 'clients/delete_client.html', {'obj': client})
