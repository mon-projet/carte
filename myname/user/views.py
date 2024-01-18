from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import *
from .serializers import *
from rest_framework import filters 

class UtilisateurApi(viewsets.ModelViewSet):
    queryset =Utilisateur.objects.all()
    serializer_class=UtilisateurSerializer

class CarteApi(viewsets.ModelViewSet):
    queryset =Cartes.objects.all()
    serializer_class=CarteSerializer

class Recherche(viewsets.ModelViewSet):
    search_fields=['numero_cni','nom']
    filter_backends=(filters.SearchFilter,) 
    queryset =Cartes.objects.all()
    serializer_class=CarteSerializer  
    