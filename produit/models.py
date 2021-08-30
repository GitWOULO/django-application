from django.db import models

# Create your models here.
class Tag(models.Model):
    nom=models.CharField(max_length=200,null=False)
    description=models.TextField(null=True)
    def __str__(self):
        return self.nom

class Produit(models.Model):
    CATEGORIE=(('Composant électronique','Composant électronique'),
                ('Plastique','Plastique'),
                ('Ordinateur bureautique','Ordinateur bureautique'),
                ('Ordinateur portable','Ordinateur portable'),
                ('Ustensile de cuisine','Ustensile de cuisine'),
                ('Aliments','Aliments'),
                ('Matériel de construction','Matériel de construction'),
                ('Moyen de transport','Moyen de transport'),               
            )
    titre=models.CharField(max_length=50,null=False)
    picture=models.CharField(null=True,max_length=400)
    prix=models.FloatField(null=True)    
    tag=models.ManyToManyField(Tag)
    categorie=models.CharField(max_length=100, null=True,choices=CATEGORIE)
    description=models.TextField(null=True)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.titre

