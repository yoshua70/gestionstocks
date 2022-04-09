from .models import Client
from django.forms import ModelForm, Select, TextInput, Textarea


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'nom': TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            }),
            'prenom': TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            }),
            'email': TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            }),
            'typeClient': Select(attrs={
                'class': "border rounded w-full"
            }, choices=['PERSONNE', 'ENTREPRISE']),
            'note': Textarea(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline h-10 resize-y",
                'style': 'min-height: 100px;',
                'placeholder': "Description"
            }),
            'pays': Select(attrs={
                'class': "border rounded w-full"
            }),
            'ville': TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            }),
            'adresse': TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            }),
        }
