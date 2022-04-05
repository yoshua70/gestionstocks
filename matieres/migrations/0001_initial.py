# Generated by Django 4.0.3 on 2022-04-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MatierePremiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeMatiere', models.CharField(max_length=50, unique=True)),
                ('libelleMatiere', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('ENSTOCK', 'En Stock'), ('RUPTURE', 'En rupture')], max_length=10)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]