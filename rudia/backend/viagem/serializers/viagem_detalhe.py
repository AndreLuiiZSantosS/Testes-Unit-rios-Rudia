from rest_framework import serializers
from viagem.models import Viagem
from localizacao.serializers import CidadeResumoSerializer
from usuarios.serializers import RudieroResumoSerializer
from servicos.serializers import ServicoResumoSerializer


class ViagemDetalheSerializer(serializers.ModelSerializer):
    """
    Serializer completo para detalhamento de viagens
    """
    rudiero = RudieroResumoSerializer(read_only=True)
    cidade_destino = CidadeResumoSerializer(read_only=True)
    servicos = serializers.SerializerMethodField()
    total_viajantes = serializers.SerializerMethodField()
    
    class Meta:
        model = Viagem
        fields = [
            'id',
            'nome',
            'descricao',
            'dias',
            'orcamento_total',
            'viajantes_adultos',
            'viajantes_criancas',
            'total_viajantes',
            'visibilidade',
            'data_criacao',
            'rudiero',
            'cidade_destino',
            'servicos'
        ]
    
    def get_total_viajantes(self, obj):
        """Retorna total de viajantes (adultos + crianças)"""
        return obj.viajantes_adultos + obj.viajantes_criancas
    
    def get_servicos(self, obj):
        """
        Agrupa serviços por categoria para facilitar visualização
        """
        servicos = obj.servicos.all()
        
        servicos_agrupados = {
            'hospedagem': None,
            'transporte': None,
            'alimentacao': [],
            'lazer': []
        }
        
        for servico in servicos:
            categoria_nome = servico.categoria.nome

            servico_data = ServicoResumoSerializer(
                servico,
                context=self.context
            ).data
            
            if categoria_nome == 'Hospedagem':
                servicos_agrupados['hospedagem'] = servico_data
            elif categoria_nome == 'Transporte':
                servicos_agrupados['transporte'] = servico_data
            elif categoria_nome == 'Alimentação':
                servicos_agrupados['alimentacao'].append(servico_data)
            elif categoria_nome == 'Lazer':
                servicos_agrupados['lazer'].append(servico_data)
        
        return servicos_agrupados