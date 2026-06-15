from rest_framework import serializers
from django.db.models import Avg
from servicos.models import Servico


class ServicoListaSerializer(serializers.ModelSerializer):
    """Serializer para listagem de serviços com informações resumidas"""
    
    # Campos calculados
    avaliacao_geral = serializers.SerializerMethodField(read_only=True)
    preco_medio = serializers.SerializerMethodField(read_only=True)
    imagem_capa_url = serializers.SerializerMethodField(read_only=True)
    
    # Informações relacionadas
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    cidade_nome = serializers.CharField(source='cidade.nome', read_only=True)
    cidade_estado = serializers.CharField(source='cidade.estado.sigla', read_only=True)
    
    class Meta:
        model = Servico
        fields = [
            'id',
            'nome',
            'descricao',
            'imagem_capa_url',
            'avaliacao_geral',
            'preco_medio',
            'categoria_nome',
            'cidade_nome',
            'cidade_estado',
        ]
        read_only_fields = ['id']
    
    def get_avaliacao_geral(self, obj):
        """
        Retorna a média das avaliações do serviço.
        """
        if hasattr(obj, 'avaliacao_geral'):
            return round(obj.avaliacao_geral, 1) if obj.avaliacao_geral else 0
        
        media = obj.avaliacoes.aggregate(media=Avg('nota'))['media']
        return round(media, 1) if media else 0
    
    def get_preco_medio(self, obj):
        """
        Retorna a média entre o preço mínimo e preço máximo do serviço
        """
        if obj.preco_minimo is not None and obj.preco_maximo is not None:
            preco_medio = (obj.preco_minimo + obj.preco_maximo) / 2
            return round(float(preco_medio), 2)
        return 0
    
    def get_imagem_capa_url(self, obj):
        """
        Retorna a URL completa da imagem de capa
        """
        request = self.context.get('request')
        if obj.imagem_capa and request:
            return request.build_absolute_uri(obj.imagem_capa.url)
        return None
