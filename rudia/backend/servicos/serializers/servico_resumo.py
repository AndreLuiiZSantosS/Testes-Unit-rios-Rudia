from rest_framework import serializers

class ServicoResumoSerializer(serializers.Serializer):
    """Serializer resumido de serviço para viagens"""
    id = serializers.IntegerField()
    nome = serializers.CharField()
    categoria = serializers.CharField(source='categoria.nome')
    preco_medio = serializers.SerializerMethodField()
    imagem_capa_url = serializers.SerializerMethodField()
    parceiro = serializers.SerializerMethodField()
    
    def get_preco_medio(self, obj):
        """Calcula preço médio do serviço"""
        return float((obj.preco_minimo + obj.preco_maximo) / 2)
    
    def get_imagem_capa_url(self, obj):
        """Retorna URL completa da imagem"""
        request = self.context.get('request')
        if obj.imagem_capa and request:
            return request.build_absolute_uri(obj.imagem_capa.url)
        return None
    
    def get_parceiro(self, obj):
        """Retorna dados do parceiro"""
        return {
            'id': obj.parceiro.id,
            'username': obj.parceiro.username
        }