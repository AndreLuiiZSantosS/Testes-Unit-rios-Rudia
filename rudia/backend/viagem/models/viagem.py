from django.db import models
from usuarios.models import Rudiero
from localizacao.models import Cidade
from servicos.models import Servico

class Viagem(models.Model):
    class Visibilidade(models.TextChoices):
        PUBLICO = 'PUBLICO', 'Público'
        PRIVADO = 'PRIVADO', 'Privado'

    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    dias = models.PositiveIntegerField()
    orcamento_total = models.DecimalField(max_digits=10, decimal_places=2)
    viajantes_adultos = models.PositiveIntegerField(default=1)
    viajantes_criancas = models.PositiveIntegerField(default=0)
    visibilidade = models.CharField(max_length=10, choices=Visibilidade.choices, default=Visibilidade.PRIVADO)
    data_criacao = models.DateTimeField(auto_now_add=True)
    rudiero = models.ForeignKey(Rudiero, on_delete=models.CASCADE, related_name='viagens')
    cidade_destino = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='viagens_destino')
    servicos = models.ManyToManyField(Servico, related_name='viagens')
    
    def __str__(self):
        return f'{self.nome} - @{self.rudiero.username}'
    
    class Meta:
        db_table = 'viagem'
        ordering = ['nome', '-data_criacao']
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'
