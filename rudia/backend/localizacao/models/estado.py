from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self) -> str:
        return f"{self.nome} ({self.sigla})"
    
    class Meta:
        db_table = 'estado'
        ordering = ['nome']
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
