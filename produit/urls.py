from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index), #on considère l'application produit comme la page d'accueil     
    path('ajouter/',views.ajouter),
    path('modifier/<str:pk>/',views.modifier,name='modifier_produit'),
]   
