from django.db import models
from .categoria import Categoria

class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='tags')

    def __str__(self) -> str:
        return f'Tag: {self.nome} (Categoria: {self.categoria.nome})'

    class Meta:
        db_table = 'tag'
        ordering = ['nome', 'categoria__nome']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        constraints = [
            models.UniqueConstraint(
                fields=['nome', 'categoria'],
                name='tag_unico_nome_categoria'
            )
        ]
