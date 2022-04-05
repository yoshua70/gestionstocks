from django.forms import ChoiceField, ModelForm, Select, TextInput, Textarea
from .models import Produit, MatierePremiere

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
        widgets = {
            'designation': TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': "Designation"
            }),
            'libelle': TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': "Libelle"
            }),
            'description': Textarea(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline h-10 resize-y",
                'style': 'min-height: 100px;',
                'placeholder': "Description"
            }),
            'statut': Select(attrs={
                'class': "border rounded w-full"
            }, choices=['ENSTOCK', 'RUPTURE'])
        }

class MatierePremiereForm(ModelForm):
    class Meta:
        model = MatierePremiere
        fields = "__all__"
        widgets = {
            'codeMatiere':TextInput(attrs={

            }),
            'libelleMatiere':TextInput(attrs={

            }),
            'status':Select(attrs={

            },choices=['En Stock', 'En rupture'])
        }