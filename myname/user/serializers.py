from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import*



class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields='__all__'

class CarteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartes
        fields='__all__'        