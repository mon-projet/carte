# Generated by Django 4.2.2 on 2023-06-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_carte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='numero_telephone',
            field=models.IntegerField(default=0),
        ),
    ]