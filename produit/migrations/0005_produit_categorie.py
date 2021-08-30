# Generated by Django 3.2.5 on 2021-07-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0004_tag_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='categorie',
            field=models.CharField(choices=[('Composant électronique', 'Composant électronique'), ('Plastique', 'Plastique'), ('Ordinateur bureautique', 'Ordinateur bureautique'), ('Ordinateur portable', 'Ordinateur portable'), ('Ustensil de cuisine', 'Ustensil de cuisine'), ('Aliments', 'Aliments'), ('Matériel de construction', 'Matériel de construction'), ('Moyen de transport', 'Moyen de transport')], max_length=100, null=True),
        ),
    ]
