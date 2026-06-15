from rest_framework import serializers
from avaliacoes.models import Avaliacao
from usuarios.serializers.usuario import UsuarioDetalheSerializer

class AvaliacaoSerializer(serializers.ModelSerializer):
    """Serializer para detalhes de avaliações"""
    rudiero = UsuarioDetalheSerializer(read_only=True)
    objeto_avaliado = serializers.SerializerMethodField(read_only=True)
    tipo_objeto = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Avaliacao
        fields = [
            'id',
            'nota',
            'comentario',
            'data_avaliacao',
            'rudiero',
            'tipo_objeto',
            'objeto_avaliado',
        ]
        read_only_fields = ['id', 'data_avaliacao', 'rudiero']
    
    def get_tipo_objeto(self, obj):
        """Retorna o tipo do objeto avaliado (Servico ou Roteiro)"""
        if obj.content_type:
            return obj.content_type.model
        return None
    
    def get_objeto_avaliado(self, obj):
        """Retorna informações básicas do objeto avaliado"""
        if not obj.content_object:
            return None
        
        content_obj = obj.content_object
        model_name = obj.content_type.model
        
        # Se for Serviço
        if model_name == 'servico':
            return {
                'id': content_obj.id,
                'nome': content_obj.nome,
                'tipo': 'servico'
            }
        
        # Se for Roteiro
        elif model_name == 'roteiro':
            return {
                'id': content_obj.id,
                'nome': content_obj.nome,
                'tipo': 'roteiro'
            }
        
        # Fallback para outros tipos
        return {
            'id': obj.object_id,
            'tipo': model_name
        }


class AvaliacaoCreateSerializer(serializers.ModelSerializer):
    """Serializer para criação de avaliações"""
    
    class Meta:
        model = Avaliacao
        fields = [
            'id',
            'nota',
            'comentario',
            'content_type',
            'object_id',
        ]
        read_only_fields = ['id']
    
    def validate_nota(self, value):
        """Valida se a nota está entre 0 e 5"""
        if value < 0 or value > 5:
            raise serializers.ValidationError("A nota deve estar entre 0 e 5.")
        return value
    
    def validate(self, attrs):
        """Valida se o objeto avaliado existe"""
        from django.core.exceptions import ObjectDoesNotExist
        
        content_type = attrs.get('content_type')
        object_id = attrs.get('object_id')
        
        # Verifica se o objeto existe
        model_class = content_type.model_class()
        try:
            model_class.objects.get(pk=object_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({
                'object_id': f'{content_type.model.title()} com id {object_id} não existe.'
            })
        
        return attrs
    
    def create(self, validated_data):
        """Cria a avaliação com o rudiero do request"""
        # O rudiero será adicionado na view
        return super().create(validated_data)


class AvaliacaoResumoSerializer(serializers.ModelSerializer):
    """Serializer resumido de avaliação (para uso em nested serializers)"""
    rudiero_username = serializers.CharField(source='rudiero.username', read_only=True)
    
    class Meta:
        model = Avaliacao
        fields = [
            'id',
            'nota',
            'comentario',
            'data_avaliacao',
            'rudiero_username',
        ]
        read_only_fields = ['id', 'data_avaliacao']


class AvaliacaoPreviewSerializer(serializers.Serializer):
    """Serializer para preview de avaliação (últimas 3)"""
    id = serializers.IntegerField(read_only=True)
    nota = serializers.DecimalField(max_digits=2, decimal_places=1, read_only=True)
    comentario = serializers.CharField(read_only=True)
    rudiero_username = serializers.CharField(source='rudiero.username', read_only=True)
    rudiero_nome = serializers.CharField(source='rudiero.nome', read_only=True)
    rudiero_foto = serializers.SerializerMethodField(read_only=True)
    data_avaliacao = serializers.DateTimeField(read_only=True)
    
    def get_rudiero_foto(self, obj):
        """Retorna URL da foto do rudiero"""
        request = self.context.get('request')
        if obj.rudiero.foto_perfil and request:
            return request.build_absolute_uri(obj.rudiero.foto_perfil.url)
        return None