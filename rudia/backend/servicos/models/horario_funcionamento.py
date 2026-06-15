from django.db import models
from .servico import Servico

class HorarioFuncionamento(models.Model):
    class DiaSemana(models.TextChoices):
        DOMINGO = 'DOM', 'Domingo'
        SEGUNDA = 'SEG', 'Segunda-feira'
        TERCA = 'TER', 'Terça-feira'
        QUARTA = 'QUA', 'Quarta-feira'
        QUINTA = 'QUI', 'Quinta-feira'
        SEXTA = 'SEX', 'Sexta-feira'
        SABADO = 'SAB', 'Sábado'

    hora_abertura = models.TimeField()
    hora_fechamento = models.TimeField()
    dia_semana = models.CharField(max_length=3, choices=DiaSemana.choices)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='horarios_funcionamento')

    def __str__(self) -> str:
        return f'Horário de {self.servico.nome} - {self.get_dia_semana_display()}: {self.hora_abertura} às {self.hora_fechamento}'
    
    class Meta:
        db_table = 'horario_funcionamento'
        ordering = ['servico__nome', 'dia_semana']
        verbose_name = 'Horário de Funcionamento'
        verbose_name_plural = 'Horários de Funcionamento'
