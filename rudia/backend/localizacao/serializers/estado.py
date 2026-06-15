from rest_framework import serializers
from localizacao.models import Estado


class EstadoSerializer(serializers.ModelSerializer):
    """Serializer para listagem e criação de Estados"""
    total_cidades = serializers.IntegerField(read_only=True, source='cidades.count')
    
    class Meta:
        model = Estado
        fields = ['id', 'nome', 'sigla', 'total_cidades']
        read_only_fields = ['id']
    
    def validate_sigla(self, value):
        """Valida e normaliza a sigla do estado"""
        sigla = value.upper().strip()
        
        if len(sigla) != 2:
            raise serializers.ValidationError("A sigla deve ter exatamente 2 caracteres.")
        
        if not sigla.isalpha():
            raise serializers.ValidationError("A sigla deve conter apenas letras.")
        
        return sigla
    
    def validate_nome(self, value):
        """Normaliza o nome do estado"""
        return value.strip().title()


class EstadoDetalheSerializer(serializers.ModelSerializer):
    """Serializer detalhado de Estado com lista de cidades"""
    cidades = serializers.SerializerMethodField()
    total_cidades = serializers.IntegerField(read_only=True, source='cidades.count')
    
    class Meta:
        model = Estado
        fields = ['id', 'nome', 'sigla', 'total_cidades', 'cidades']
        read_only_fields = ['id']
    
    def get_cidades(self, obj):
        """Retorna lista resumida de cidades do estado"""
        return [
            {
                'id': cidade.id,
                'nome': cidade.nome,
            }
            for cidade in obj.cidades.all()
        ]


class EstadoResumoSerializer(serializers.ModelSerializer):
    """Serializer resumido de Estado (para uso em nested serializers)"""
    
    class Meta:
        model = Estado
        fields = ['id', 'nome', 'sigla']
        read_only_fields = ['id']