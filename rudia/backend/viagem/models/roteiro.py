from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .viagem import Viagem

class Roteiro(models.Model):
    class Visibilidade(models.TextChoices):
        PUBLICO = 'PUBLICO', 'Público'
        PRIVADO = 'PRIVADO', 'Privado'

    data_partida = models.DateField()
    visibilidade = models.CharField(max_length=10, choices=Visibilidade.choices, default=Visibilidade.PRIVADO)
    data_criacao = models.DateTimeField(auto_now_add=True)
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name='roteiros')
    avaliacoes = GenericRelation('avaliacoes.Avaliacao', related_query_name='roteiro')


    def __str__(self):
        return f'Roteiro do dia {self.data_partida} da viagem {self.viagem.nome}'
    
    class Meta:
        db_table = 'roteiro'
        ordering = ['viagem__nome', '-data_criacao']
        verbose_name = 'Roteiro'
        verbose_name_plural = 'Roteiros'
