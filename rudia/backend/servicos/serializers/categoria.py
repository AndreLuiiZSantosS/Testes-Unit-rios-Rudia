from rest_framework import serializers
from servicos.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializer para Categoria"""
    total_servicos = serializers.IntegerField(read_only=True, source='servicos.count')
    
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'total_servicos']
        read_only_fields = ['id']
    
    def validate_nome(self, value):
        """Normaliza o nome da categoria"""
        return value.strip().title()


class CategoriaResumoSerializer(serializers.ModelSerializer):
    """Serializer resumido de Categoria (para uso em nested serializers)"""
    
    class Meta:
        model = Categoria
        fields = ['id', 'nome']
        read_only_fields = ['id']
