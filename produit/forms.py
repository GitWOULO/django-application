from django.forms import ModelForm
from .models import Produit

class FormulaireAjoutProduit(ModelForm):
    class Meta:
        model=Produit
        fields='__all__'