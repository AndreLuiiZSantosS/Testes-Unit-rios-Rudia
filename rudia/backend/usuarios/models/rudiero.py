from django.db import models
from .usuario import Usuario

class Rudiero(Usuario):
    class Genero(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        OUTRO = 'O', 'Outro'
        PREFIRO_NAO_INFORMAR = 'N', 'Prefiro Não Informar'

    data_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=Genero.choices, default=Genero.PREFIRO_NAO_INFORMAR)

    def save(self, *args, **kwargs):
        self.tipo_usuario = Usuario.TipoUsuario.RUDIERO
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Rudiero: @{self.username}'

    class Meta:
        db_table = 'rudiero'
        ordering = ['username']
        verbose_name = 'Rudiero'
        verbose_name_plural = 'Rudieros'
