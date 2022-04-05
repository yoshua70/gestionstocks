from django.forms import ChoiceField, ModelForm, Select, TextInput, Textarea
from .models import MatierePremiere
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