from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil (Interface élève)
    path('', views.index, name='index'),
    # Récupérer toutes les leçons
    path('api/lessons/', views.get_lessons_list, name='lessons_list'),
    
    # Récupérer une leçon précise grâce à son ID
    path('api/lessons/<int:lesson_id>/', views.get_lesson_detail, name='lesson_detail'),
]