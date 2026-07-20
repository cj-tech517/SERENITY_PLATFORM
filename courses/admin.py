from django.contrib import admin
from .models import Lesson, LessonCard

class LessonCardInline(admin.TabularInline):
    """
    Permet d'ajouter, modifier ou supprimer des cartes interactives 
    directement depuis la page de gestion de la Leçon associée.
    """
    model = LessonCard
    extra = 3  # Django affichera automatiquement 3 formulaires de cartes vides
    fields = ('title_or_word', 'definition_or_content', 'example', 'card_visual')
    verbose_name = "Carte interactive"
    verbose_name_plural = "Cartes associées à cette leçon"


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour les Leçons.
    """
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'instructions_text')
    
    # Intégration des cartes en ligne
    inlines = [LessonCardInline]
    
    fieldsets = (
        ("Informations Générales", {
            # Changement ici : on remplace 'video_url' par 'video_embed_code'
            'fields': ('title', 'category', 'video_embed_code', 'visual', 'description')
        }),
        ("Mission & Devoirs pour l'élève", {
            'fields': ('instructions_title', 'instructions_text'),
            'description': 'Configure les consignes de travail demandées à l\'élève pour cette leçon.'
        }),
    )