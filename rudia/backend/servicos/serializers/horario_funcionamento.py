from rest_framework import serializers
from servicos.models import HorarioFuncionamento


class HorarioFuncionamentoSerializer(serializers.ModelSerializer):
    """Serializer para Horários de Funcionamento"""
    dia_semana_display = serializers.CharField(source='get_dia_semana_display', read_only=True)
    
    class Meta:
        model = HorarioFuncionamento
        fields = [
            'id',
            'dia_semana',
            'dia_semana_display',
            'hora_abertura',
            'hora_fechamento'
        ]
        read_only_fields = ['id']
    
    def validate(self, data):
        """Valida que hora_fechamento é posterior a hora_abertura"""
        hora_abertura = data.get('hora_abertura')
        hora_fechamento = data.get('hora_fechamento')
        
        if hora_abertura and hora_fechamento and hora_fechamento <= hora_abertura:
            raise serializers.ValidationError(
                'A hora de fechamento deve ser posterior à hora de abertura.'
            )
        
        return data

