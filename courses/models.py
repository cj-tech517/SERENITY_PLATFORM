from django.db import models

class Lesson(models.Model):
    CATEGORY_CHOICES = [
        ('SERENITY', 'Serenity Core'),
        ('STREET_TALK', 'Street Talk Series'),
        ('SLANGMAN', 'Slangman Guide'),
    ]

    title = models.CharField(
        verbose_name="Titre de la leçon",
        max_length=300, 
    )
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='SERENITY', 
        verbose_name="Catégorie"
    )
    # Remplacement de video_url par video_embed_code pour accepter tout le code HTML d'intégration
    video_embed_code = models.TextField(
        blank=True,
        null=True,
        verbose_name="Code d'intégration de la vidéo (Iframe/Embed)",
        help_text="Collez ici l'intégralité du code d'intégration (ex: <iframe ...></iframe>) fourni par YouTube ou Vimeo."
    )
    
    # Détails optionnels de la leçon
    visual = models.ImageField(
        upload_to='lessons/visuals/', 
        blank=True, 
        null=True, 
        verbose_name="Image illustrative (Optionnelle)"
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Description de la leçon (Optionnelle)"
    )
    
    # Mission / Devoir pour l'élève
    instructions_title = models.CharField(
        max_length=300, 
        default="MISSION D'ACTIVATION", 
        verbose_name="Titre de la mission"
    )
    instructions_text = models.TextField(
        verbose_name="Consignes de l'exercice"
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Date de création"
    )

    class Meta:
        verbose_name = "Leçon"
        verbose_name_plural = "Leçons"
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"


class LessonCard(models.Model):
    # La relation ForeignKey lie chaque carte à une seule leçon.
    # on_delete=models.CASCADE signifie que si tu supprimes une leçon, toutes ses cartes associées sont supprimées automatiquement.
    lesson = models.ForeignKey(
        Lesson, 
        on_delete=models.CASCADE, 
        related_name='cards', 
        verbose_name="Leçon associée"
    )
    
    title_or_word = models.CharField(
        max_length=150, 
        verbose_name="Mot, expression ou concept"
    )
    definition_or_content = models.TextField(
        verbose_name="Définition ou explication"
    )
    example = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Exemple d'utilisation (Optionnel)"
    )
    
    # Visuel optionnel spécifique à la carte
    card_visual = models.ImageField(
        upload_to='lessons/cards/', 
        blank=True, 
        null=True, 
        verbose_name="Visuel de la carte (Optionnel)"
    )

    class Meta:
        verbose_name = "Carte interactive"
        verbose_name_plural = "Cartes interactives"

    def __str__(self):
        return f"Carte : {self.title_or_word} (Leçon : {self.lesson.title})"