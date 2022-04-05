from django.forms import ModelForm, Select, TextInput
from .models import MatierePremiere


class MatierePremiereForm(ModelForm):
    class Meta:
        model = MatierePremiere
        fields = "__all__"
        widgets = {
            'codeMatiere': TextInput(attrs={

            }),
            'libelleMatiere': TextInput(attrs={

            }),
            'status': Select(attrs={

            }, choices=['En Stock', 'En rupture'])
        }
