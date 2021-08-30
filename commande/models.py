from django.db import models
from client.models import Client
from produit.models import Produit
# Create your models here.   

class Commande(models.Model):
    STATUS=(('En instance','En instance'),
        ('Livré','Livré'),
        ('Non livré','Non livré'))
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    client=models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    produit=models.ForeignKey(Produit,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.status   
