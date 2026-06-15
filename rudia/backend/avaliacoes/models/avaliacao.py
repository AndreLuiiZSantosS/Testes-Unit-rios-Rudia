from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Rudiero

class Avaliacao(models.Model):    
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    comentario = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)
    rudiero = models.ForeignKey(Rudiero, on_delete=models.CASCADE, related_name='avaliacoes')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Avaliação de {self.content_object}: {self.nota}"

    class Meta:
        db_table = 'avaliacao'
        ordering = ['-data_avaliacao']
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['rudiero', 'content_type', 'object_id'],
                name='avaliacao_unica_por_rudiero'
            )
        ]
