from rest_framework import serializers
from localizacao.models import Cidade, Estado
from .estado import EstadoResumoSerializer


class CidadeListaSerializer(serializers.ModelSerializer):
    """Serializer para listagem de Cidades"""
    estado = EstadoResumoSerializer(read_only=True)
    total_imagens = serializers.IntegerField(read_only=True, source='imagens.count')
    
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado', 'total_imagens']
        read_only_fields = ['id']


class CidadeCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer para criação e atualização de Cidades"""
    
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado']
        read_only_fields = ['id']
    
    def validate_nome(self, value):
        """Normaliza o nome da cidade"""
        return value.strip().title()
    
    def validate(self, attrs):
        """Valida se já existe cidade com o mesmo nome no estado"""
        nome = attrs.get('nome')
        estado = attrs.get('estado')
        
        # Se for atualização, exclui a própria instância da validação
        instance = self.instance
        query = Cidade.objects.filter(nome=nome, estado=estado)
        
        if instance:
            query = query.exclude(pk=instance.pk)
        
        if query.exists():
            raise serializers.ValidationError({
                'nome': f'Já existe uma cidade chamada "{nome}" no estado {estado.sigla}.'
            })
        
        return attrs


class CidadeDetalheSerializer(serializers.ModelSerializer):
    """Serializer detalhado de Cidade com imagens"""
    estado = EstadoResumoSerializer(read_only=True)
    imagens = serializers.SerializerMethodField()
    total_imagens = serializers.IntegerField(read_only=True, source='imagens.count')
    
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado', 'total_imagens', 'imagens']
        read_only_fields = ['id']
    
    def get_imagens(self, obj):
        """Retorna lista de imagens da cidade"""
        request = self.context.get('request')
        return [
            {
                'id': imagem.id,
                'caminho_imagem': request.build_absolute_uri(imagem.caminho_imagem.url) if imagem.caminho_imagem else None,
                'data_inclusao': imagem.data_inclusao,
            }
            for imagem in obj.imagens.all()
        ]


class CidadeResumoSerializer(serializers.ModelSerializer):
    """Serializer resumido de Cidade (para uso em nested serializers)"""
    estado_sigla = serializers.CharField(source='estado.sigla', read_only=True)
    
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado_sigla']
        read_only_fields = ['id']