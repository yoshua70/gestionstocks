from typing import Text
from django.forms import ModelForm, TextInput, Textarea
from .models import Produit

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
        widgets = {
            'designation': TextInput(attrs={
                'class': "shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': "Designation"
            }),
            'libelle': TextInput(attrs={
                'class': "shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': "Libelle"
            }),
            'description': Textarea(attrs={
                'class': "shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline h-10 resize-y",
                'style': 'min-height: 100px;',
                'placeholder': "Description"
            })
        }