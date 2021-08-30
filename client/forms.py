from django.forms import ModelForm
from .models import Client

class FormulaireAjoutClient(ModelForm):
    class Meta:
        model=Client
        fields='__all__'