from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Usuario

class Proposta(models.Model):
    class StatusProposta(models.TextChoices):
        EM_ANALISE = 'EA', 'Em Análise'
        APROVADA = 'AP', 'Aprovada'
        REPROVADA = 'RP', 'Reprovada'

    comentario_moderador = models.TextField(blank=True, null=True)
    status_proposta = models.CharField(
        max_length=2, 
        choices=StatusProposta.choices, 
        default=StatusProposta.EM_ANALISE
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_analise = models.DateTimeField(blank=True, null=True)
    moderador = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        related_name='propostas_analisadas',
        blank=True,
        null=True,
        limit_choices_to={'tipo_usuario__in': ['MODERADOR', 'ADMINISTRADOR']}
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self) -> str:
        tipo = self.content_type.model_class().__name__
        return f"Proposta de {tipo} - Status: {self.get_status_proposta_display()}"

    class Meta:
        db_table = 'proposta'
        ordering = ['status_proposta', '-data_criacao']
        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
            models.Index(fields=['status_proposta', 'data_criacao']),
        ]