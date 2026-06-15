from rest_framework import serializers
from django.db import transaction
from drf_extra_fields.fields import Base64ImageField
from servicos.models import Servico, Categoria, Tag, HorarioFuncionamento
from moderacao.models import Proposta
from localizacao.models import Cidade, Endereco
from localizacao.serializers import EnderecoSerializer
from servicos.serializers.horario_funcionamento import HorarioFuncionamentoSerializer


class ServicoCreateSerializer(serializers.ModelSerializer):
    """Serializer para criação de Serviços com objetos relacionados"""

    imagem_capa = Base64ImageField()
    
    # Nested serializers para criação
    endereco = EnderecoSerializer()
    horarios_funcionamento = HorarioFuncionamentoSerializer(many=True)
    
    # Chaves primárias para relacionamentos
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    cidade = serializers.PrimaryKeyRelatedField(queryset=Cidade.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    
    class Meta:
        model = Servico
        fields = [
            'id',
            'nome',
            'descricao',
            'capacidade_maxima',
            'preco_minimo',
            'preco_maximo',
            'imagem_capa',
            'categoria',
            'cidade',
            'tags',
            'endereco',
            'horarios_funcionamento'
        ]
        read_only_fields = ['id']
    
    def validate(self, data):
        """Validações customizadas"""
        # Valida preços
        preco_minimo = data.get('preco_minimo')
        preco_maximo = data.get('preco_maximo')
        
        if preco_minimo and preco_maximo and preco_maximo < preco_minimo:
            raise serializers.ValidationError({
                'preco_maximo': 'O preço máximo deve ser maior ou igual ao preço mínimo.'
            })
        
        # Valida capacidade
        capacidade_maxima = data.get('capacidade_maxima')
        if capacidade_maxima and capacidade_maxima <= 0:
            raise serializers.ValidationError({
                'capacidade_maxima': 'A capacidade máxima deve ser maior que zero.'
            })
        
        # Valida que as tags pertencem à categoria
        categoria = data.get('categoria')
        tags = data.get('tags', [])
        
        if categoria and tags:
            tags_invalidas = [tag for tag in tags if tag.categoria_id != categoria.id]
            if tags_invalidas:
                raise serializers.ValidationError({
                    'tags': f'As tags devem pertencer à categoria selecionada ({categoria.nome}).'
                })
        
        # Valida horários únicos (sem duplicatas de dia_semana)
        horarios = data.get('horarios_funcionamento', [])
        dias_semana = [h['dia_semana'] for h in horarios]
        
        if len(dias_semana) != len(set(dias_semana)):
            raise serializers.ValidationError({
                'horarios_funcionamento': 'Não pode haver horários duplicados para o mesmo dia da semana.'
            })
        
        return data
    
    @transaction.atomic
    def create(self, validated_data):
        """Cria o serviço e todos os objetos relacionados atomicamente"""
        # Extrai dados nested
        endereco_data = validated_data.pop('endereco')
        horarios_data = validated_data.pop('horarios_funcionamento')
        tags_data = validated_data.pop('tags')
        
        # Obtém o parceiro do request
        parceiro = self.context['request'].user.parceiro
        
        # 1. Cria o endereço
        endereco = Endereco.objects.create(**endereco_data)
        
        # 2. Cria o serviço
        servico = Servico.objects.create(
            **validated_data,
            endereco=endereco,
            parceiro=parceiro,
            ativo=False
        )
        
        # 3. Adiciona as tags
        servico.tags.set(tags_data)
        
        # 4. Cria os horários de funcionamento
        for horario_data in horarios_data:
            HorarioFuncionamento.objects.create(
                servico=servico,
                **horario_data
            )
        
        # 5. Cria a proposta
        Proposta.objects.create(content_object=servico)
        
        return servico
