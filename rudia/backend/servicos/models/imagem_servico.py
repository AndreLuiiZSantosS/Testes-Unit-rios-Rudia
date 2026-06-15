from django.db import models
from .servico import Servico

class ImagemServico(models.Model):
    caminho_imagem = models.ImageField(upload_to='imagens_servicos/')
    data_inclusao = models.DateTimeField(auto_now_add=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='imagens_servico')

    def __str__(self) -> str:
        return f'Imagem do Serviço: {self.servico.nome}'
    
    class Meta:
        db_table = 'imagem_servico'
        ordering = ['servico__nome']
        verbose_name = 'Imagem do Serviço'
        verbose_name_plural = 'Imagens dos Serviços'
