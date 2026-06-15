from django.db import models
from .cidade import Cidade

class ImagemCidade(models.Model):
    caminho_imagem = models.ImageField(upload_to='imagens_cidades/')
    data_inclusao = models.DateTimeField(auto_now_add=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='imagens')

    def __str__(self):
        return f'Imagem da Cidade {self.cidade.nome}'
    
    class Meta:
        db_table = 'imagem_cidade'
        ordering = ['cidade__nome']
        verbose_name = 'Imagem da Cidade'
        verbose_name_plural = 'Imagens das Cidades'
