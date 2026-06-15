from rest_framework import serializers
from django.db import transaction
from decimal import Decimal
from viagem.models import Viagem
from servicos.models import Servico
from localizacao.models import Cidade


class ViagemCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para criação de Viagens com validações de serviços
    
    Regras de Negócio:
    - Obrigatório: 1 hospedagem, 1 transporte
    - Obrigatório: pelo menos 1 alimentação, 1 lazer
    - Serviços devem ser da mesma cidade
    - Serviços devem ter capacidade >= total viajantes (quando aplicável)
    - Serviços devem estar ativos
    - Orçamento é calculado automaticamente
    """
    
    hospedagem = serializers.PrimaryKeyRelatedField(
        queryset=Servico.objects.filter(ativo=True),
        required=True,
        error_messages={
            'required': 'É obrigatório selecionar um serviço de hospedagem.',
            'does_not_exist': 'Serviço de hospedagem não encontrado ou inativo.'
        }
    )
    
    transporte = serializers.PrimaryKeyRelatedField(
        queryset=Servico.objects.filter(ativo=True),
        required=True,
        error_messages={
            'required': 'É obrigatório selecionar um serviço de transporte.',
            'does_not_exist': 'Serviço de transporte não encontrado ou inativo.'
        }
    )
    
    alimentacao = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Servico.objects.filter(ativo=True),
        required=True,
        error_messages={
            'required': 'É obrigatório selecionar pelo menos um serviço de alimentação.',
            'empty': 'É obrigatório selecionar pelo menos um serviço de alimentação.'
        }
    )
    
    lazer = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Servico.objects.filter(ativo=True),
        required=True,
        error_messages={
            'required': 'É obrigatório selecionar pelo menos um serviço de lazer.',
            'empty': 'É obrigatório selecionar pelo menos um serviço de lazer.'
        }
    )
    
    cidade_destino = serializers.PrimaryKeyRelatedField(
        queryset=Cidade.objects.all(),
        required=True
    )
    
    orcamento_total = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )
    
    class Meta:
        model = Viagem
        fields = [
            'id',
            'nome',
            'descricao',
            'dias',
            'viajantes_adultos',
            'viajantes_criancas',
            'visibilidade',
            'cidade_destino',
            'hospedagem',
            'transporte',
            'alimentacao',
            'lazer',
            'orcamento_total',
            'data_criacao'
        ]
        read_only_fields = ['id', 'orcamento_total', 'data_criacao']
    
    def validate_dias(self, value):
        """Valida que a quantidade de dias é positiva"""
        if value <= 0:
            raise serializers.ValidationError('A quantidade de dias deve ser maior que zero.')
        return value
    
    def validate_viajantes_adultos(self, value):
        """Valida que há pelo menos um adulto"""
        if value <= 0:
            raise serializers.ValidationError('Deve haver pelo menos um viajante adulto.')
        return value
    
    def validate_alimentacao(self, value):
        """Valida que há pelo menos um serviço de alimentação"""
        if not value or len(value) == 0:
            raise serializers.ValidationError('É obrigatório selecionar pelo menos um serviço de alimentação.')
        return value
    
    def validate_lazer(self, value):
        """Valida que há pelo menos um serviço de lazer"""
        if not value or len(value) == 0:
            raise serializers.ValidationError('É obrigatório selecionar pelo menos um serviço de lazer.')
        return value
    
    def validate(self, data):
        """
        Validações complexas envolvendo múltiplos campos
        """
        hospedagem = data.get('hospedagem')
        transporte = data.get('transporte')
        alimentacao = data.get('alimentacao', [])
        lazer = data.get('lazer', [])
        cidade_destino = data.get('cidade_destino')
        dias = data.get('dias')
        total_viajantes = data.get('viajantes_adultos', 0) + data.get('viajantes_criancas', 0)
        
        todos_servicos = [hospedagem, transporte] + list(alimentacao) + list(lazer)
        
        self._validar_categorias(hospedagem, transporte, alimentacao, lazer)
        
        self._validar_cidade(todos_servicos, cidade_destino)
        
        self._validar_capacidade(todos_servicos, total_viajantes)
        
        self._validar_status_ativo(todos_servicos)
        
        data['orcamento_total'] = self._calcular_orcamento(todos_servicos, dias)
        
        return data
    
    def _validar_categorias(self, hospedagem, transporte, alimentacao, lazer):
        """Valida que os serviços pertencem às categorias corretas"""
        errors = {}
        
        if hospedagem and hospedagem.categoria.nome != 'Hospedagem':
            errors['hospedagem'] = f'O serviço selecionado não é da categoria Hospedagem.'
        
        if transporte and transporte.categoria.nome != 'Transporte':
            errors['transporte'] = f'O serviço selecionado não é da categoria Transporte.'
        
        for servico in alimentacao:
            if servico.categoria.nome != 'Alimentação':
                errors['alimentacao'] = f'Um ou mais serviços selecionados não são da categoria Alimentação.'
                break
        
        for servico in lazer:
            if servico.categoria.nome != 'Lazer':
                errors['lazer'] = f'Um ou mais serviços selecionados não são da categoria Lazer.'
                break
        
        if errors:
            raise serializers.ValidationError(errors)
    
    def _validar_cidade(self, servicos, cidade_destino):
        """Valida que todos os serviços são da mesma cidade"""
        servicos_cidade_diferente = [
            s for s in servicos if s.cidade_id != cidade_destino.id
        ]
        
        if servicos_cidade_diferente:
            raise serializers.ValidationError({
                'servicos': f'Todos os serviços devem pertencer à cidade de destino ({cidade_destino.nome}).'
            })
    
    def _validar_capacidade(self, servicos, total_viajantes):
        """Valida que os serviços têm capacidade para o total de viajantes"""
        servicos_capacidade_insuficiente = []
        
        for servico in servicos:
            # Só valida se o serviço tem capacidade_maxima definida
            if servico.capacidade_maxima is not None:
                if servico.capacidade_maxima < total_viajantes:
                    servicos_capacidade_insuficiente.append(
                        f'{servico.nome} (capacidade: {servico.capacidade_maxima})'
                    )
        
        if servicos_capacidade_insuficiente:
            raise serializers.ValidationError({
                'servicos': f'Os seguintes serviços não têm capacidade para {total_viajantes} viajantes: {", ".join(servicos_capacidade_insuficiente)}'
            })
    
    def _validar_status_ativo(self, servicos):
        """Valida que todos os serviços estão ativos"""
        servicos_inativos = [s.nome for s in servicos if not s.ativo]
        
        if servicos_inativos:
            raise serializers.ValidationError({
                'servicos': f'Os seguintes serviços estão inativos: {", ".join(servicos_inativos)}'
            })
    
    def _calcular_orcamento(self, servicos, dias):
        """
        Calcula o orçamento total baseado nos serviços e quantidade de dias
        
        Fórmula: (preço_médio_servico * dias) para cada serviço
        preço_médio = (preco_minimo + preco_maximo) / 2
        """
        orcamento_total = Decimal('0.00')
        
        for servico in servicos:
            preco_medio = (servico.preco_minimo + servico.preco_maximo) / 2
            custo_servico = preco_medio * dias
            orcamento_total += custo_servico
        
        return round(orcamento_total, 2)
    
    @transaction.atomic
    def create(self, validated_data):
        """
        Cria a viagem e associa os serviços atomicamente
        """
        hospedagem = validated_data.pop('hospedagem')
        transporte = validated_data.pop('transporte')
        alimentacao = validated_data.pop('alimentacao')
        lazer = validated_data.pop('lazer')
        
        rudiero = self.context['request'].user.rudiero
        
        viagem = Viagem.objects.create(
            **validated_data,
            rudiero=rudiero
        )
        
        todos_servicos = [hospedagem, transporte] + list(alimentacao) + list(lazer)
        
        viagem.servicos.set(todos_servicos)
        
        return viagem