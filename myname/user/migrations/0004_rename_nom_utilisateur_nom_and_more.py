# Generated by Django 4.2.2 on 2023-07-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_utilisateur_numero_telephone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='nom',
            new_name='Nom',
        ),
        migrations.AlterField(
            model_name='carte',
            name='date_naissance',
            field=models.CharField(max_length=10),
        ),
    ]