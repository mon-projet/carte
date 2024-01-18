
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from rest_framework import routers
from user import views as userviews  
from django.conf.urls.static import static

router=routers.DefaultRouter()
router.register(r'Utilisateur',userviews.UtilisateurApi, 'utilisateur')
router.register(r'Cartes',userviews.CarteApi, 'cartes')
router.register(r'Recherche',userviews.Recherche,'Recherche')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    url(r'^api/',include(router.urls)),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)