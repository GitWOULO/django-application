# Generated by Django 3.2.5 on 2021-07-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_auto_20210727_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='tag',
            field=models.ManyToManyField(to='produit.Tag'),
        ),
    ]
