<<<<<<< HEAD:base/forms.py
from django.forms import ChoiceField, ModelForm, Select, TextInput, Textarea
from .models import Produit
=======
from django.forms import ModelForm, Select, TextInput, Textarea
from .models import Produit

>>>>>>> de8943b1c6d5980c8aeae62bacd6828142451c5b:produits/forms.py

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
<<<<<<< HEAD:base/forms.py

=======
>>>>>>> de8943b1c6d5980c8aeae62bacd6828142451c5b:produits/forms.py
