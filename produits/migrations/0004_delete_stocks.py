# Generated by Django 4.0.3 on 2022-04-05 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0003_alter_produit_designation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stocks',
        ),
    ]
