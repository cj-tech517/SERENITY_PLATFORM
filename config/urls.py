from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # L'accès classique et fonctionnel à ton panneau d'administration
    path('admin/', admin.site.urls), 
    
    # On connecte les routes de notre application "courses"
    path('', include('courses.urls')),           
]

# Permet à Django de servir tes images d'illustration et de cartes en local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)