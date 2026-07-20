from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Lesson

def index(request):
    """
    Affiche la page d'accueil de la plateforme (l'interface élève en JS).
    """
    return render(request, 'courses/index.html')


def get_lessons_list(request):
    """
    Renvoie la liste de toutes les leçons (ID, titre, catégorie)
    pour alimenter la barre latérale (sidebar) de navigation de l'élève.
    """
    # Récupère toutes les leçons triées par date de création
    lessons = Lesson.objects.all().order_by('created_at')
    data = []
    for lesson in lessons:
        data.append({
            'id': lesson.id,
            'title': lesson.title,
            'category': lesson.get_category_display(),
        })
    return JsonResponse({'lessons': data}, safe=False)


def get_lesson_detail(request, lesson_id):
    """
    Renvoie tous les détails d'une leçon spécifique (vidéo, consignes, description)
    ains que l'intégralité de ses cartes contenant les visuels absolus et les exemples.
    """
    lesson = get_object_or_404(Lesson, id=lesson_id)
    
    # On prépare la liste des cartes associées
    cards_data = []
    for card in lesson.cards.all():
        # Génération d'une URL absolue complète pour l'image de la carte (ex: http://127.0.0.1:8000/media/...)
        card_visual_url = None
        if card.card_visual:
            card_visual_url = request.build_absolute_uri(card.card_visual.url)

        cards_data.append({
            'title_or_word': card.title_or_word,
            'definition_or_content': card.definition_or_content,
            'example': card.example or "",
            'card_visual': card_visual_url,
        })
        
    # Génération d'une URL absolue complète pour le visuel de la leçon si présent
    lesson_visual_url = None
    if lesson.visual:
        lesson_visual_url = request.build_absolute_uri(lesson.visual.url)

    # On assemble l'ensemble des données de la leçon
    response_data = {
        'id': lesson.id,
        'title': lesson.title,
        'category': lesson.get_category_display(),
        'video_embed_code': lesson.video_embed_code or "",
        'visual': lesson_visual_url,
        'description': lesson.description or "",
        'instructions_title': lesson.instructions_title,
        'instructions_text': lesson.instructions_text,
        'cards': cards_data, # Contient les cartes avec les URLs d'images corrigées
    }
    
    return JsonResponse(response_data)