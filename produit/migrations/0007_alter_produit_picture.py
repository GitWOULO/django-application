# Generated by Django 3.2.5 on 2021-08-17 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0006_auto_20210817_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='picture',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
