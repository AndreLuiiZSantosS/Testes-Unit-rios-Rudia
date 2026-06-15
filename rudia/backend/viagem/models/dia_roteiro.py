from django.db import models
from .roteiro import Roteiro
from servicos.models import Servico

class DiaRoteiro(models.Model):
    dia = models.PositiveIntegerField()
    roteiro = models.ForeignKey(Roteiro, on_delete=models.CASCADE, related_name='dias_roteiro')
    servicos = models.ManyToManyField(Servico, related_name='dias_roteiro')

    def __str__(self):
        return f'Dia {self.dia} do Roteiro da Viagem {self.roteiro.viagem.nome}'

    class Meta:
        db_table = 'dia_roteiro'
        ordering = ['roteiro__viagem__nome', 'dia']
        verbose_name = 'Dia do Roteiro'
        verbose_name_plural = 'Dias do Roteiro'
