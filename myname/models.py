from django.db import models

 #Create your models here.
class Utilisateur(models.Model):
    Nom = models.CharField(max_length=100)
    lieu_residence = models.CharField(max_length=100)
    numero_telephone = models.IntegerField(default=0)

class Cartes(models.Model):
    publieur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE,null=True)
    numero_cni = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    endroit_trouver = models.CharField(max_length=20)
    photo=models.ImageField(upload_to='images/')
    photo1=models.ImageField(upload_to='images/',null=True)
   