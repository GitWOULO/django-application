from django.urls import path,include
from . import views

urlpatterns = [
    path('inscription/',views.inscription,name='inscription'),
    path('access/',views.access,name='access'), 
    path('access/',views.logoutUser,name='quitter'), 
]
