from django.db import models
from usuarios.models import Parceiro
from django.contrib.contenttypes.fields import GenericRelation
from localizacao.models import Cidade, Endereco
from .categoria import Categoria
from .tag import Tag

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    capacidade_maxima = models.PositiveIntegerField(blank=True, null=True)
    preco_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=False)
    imagem_capa = models.ImageField(upload_to='fotos_servico/')
    data_admissao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    parceiro = models.ForeignKey(Parceiro, on_delete=models.CASCADE, related_name='servicos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='servicos')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='servicos')
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='servico')
    tags = models.ManyToManyField(Tag, related_name='servicos')
    avaliacoes = GenericRelation('avaliacoes.Avaliacao', related_query_name='servico')
    propostas = GenericRelation('moderacao.Proposta', related_query_name='servico')

    def __str__(self) -> str:
        return f'{self.nome} - @{self.parceiro.username} - Ativo: {"SIM" if self.ativo else "NÃO"}'
    
    class Meta:
        db_table = 'servico'
        ordering = ['nome']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        constraints = [
            models.UniqueConstraint(
                fields=['nome', 'parceiro'],
                name='servico_unico_nome_parceiro'
            )
        ]
