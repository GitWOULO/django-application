from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index), #on considère l'application produit comme la page d'accueil
    path('listing/',views.listing, name='listing_commande'),
    path('ajouter/',views.ajouter,name='ajouter_commande'),
    path('modifier/<str:pk>/',views.modifier,name='modifier_commande'),
    path('supprimer/<str:pk>/',views.supprimer,name='supprimer_commande'),
]
