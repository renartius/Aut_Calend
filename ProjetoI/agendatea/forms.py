from django import forms
from agendatea.models import Compromisso

class CompromissoForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ['data', 'hora', 'local', 'tipo', 'pessoa']
