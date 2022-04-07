# Generated by Django 4.0.3 on 2022-04-07 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matieres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matierepremiere',
            name='codeMatiere',
            field=models.CharField(max_length=50, unique=True, verbose_name='Code de la matière première'),
        ),
        migrations.AlterField(
            model_name='matierepremiere',
            name='libelleMatiere',
            field=models.CharField(max_length=100, verbose_name='Libellé de la matière'),
        ),
    ]
