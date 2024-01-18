from django.contrib import admin

# Register your models here.
from .models import Utilisateur
from .models import Cartes

admin.site.register (Utilisateur)
admin.site.register (Cartes)