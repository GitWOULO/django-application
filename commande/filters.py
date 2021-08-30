from .models import Commande
import django_filters


class CommandeFilter(django_filters.FilterSet):
    class Meta:
        model=Commande
        fields='__all__'
        exclude=['date_creation','client']