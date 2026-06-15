from django.db import models
from .estado import Estado

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='cidades')

    def __str__(self) -> str:
        return f'{self.nome} - {self.estado.sigla}'
    
    class Meta:
        db_table = 'cidade'
        ordering = ['nome', 'estado__sigla']
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        constraints = [
            models.UniqueConstraint(
                fields=['nome', 'estado'], 
                name='cidade_unico_nome_estado'
            )
        ]
