from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .usuario import Usuario

class Parceiro(Usuario):
    cnpj = models.CharField(max_length=14, unique=True)
    ativo = models.BooleanField(default=False)
    data_admissao = models.DateTimeField(blank=True, null=True)
    propostas = GenericRelation('moderacao.Proposta', related_query_name='parceiro')

    def save(self, *args, **kwargs):
        self.tipo_usuario = Usuario.TipoUsuario.PARCEIRO
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Parceiro: @{self.username} - Ativo: {'SIM' if self.ativo else 'NÃO'}"
    
    class Meta:
        db_table = 'parceiro'
        ordering = ['username']
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'
