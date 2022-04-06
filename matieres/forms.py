from django.forms import ModelForm, Select, TextInput, Textarea
from .models import MatierePremiere


class MatierePremiereForm(ModelForm):
    class Meta:
        model = MatierePremiere
        fields = "__all__"
        widgets = {
            'codeMatiere': TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': "Code unique de la matière première"
            }),
            'libelleMatiere': TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': "Libelle"
            }),
            'description': Textarea(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline h-10 resize-y",
                'style': 'min-height: 100px;',
                'placeholder': "Description"                
            }),
            'status': Select(attrs={

            }, choices=['En Stock', 'En rupture'])
        }
