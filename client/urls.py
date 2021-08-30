from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index), #on considère l'application produit comme la page d'accueil    
    path('listing/',views.listing,name='listing'),
    path('profil/<str:pk>/',views.profil_client,name='profil_client'),
    path('creation/',views.creer_client,name='creer_client'), 
    path('modifier/<str:pk>/',views.modifier_client,name='modifier_client'),    
    path('supprimer/<str:pk>/',views.supprimer_client,name='supprimer_client'),   
]