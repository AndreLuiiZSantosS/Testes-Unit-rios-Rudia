from rest_framework import serializers
from localizacao.models import ImagemCidade, Cidade
from .cidade import CidadeResumoSerializer


class ImagemCidadeSerializer(serializers.ModelSerializer):
    """Serializer para criação e listagem de Imagens de Cidade"""
    cidade_info = CidadeResumoSerializer(source='cidade', read_only=True)
    caminho_imagem_url = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = ImagemCidade
        fields = [
            'id',
            'caminho_imagem',
            'caminho_imagem_url',
            'data_inclusao',
            'cidade',
            'cidade_info'
        ]
        read_only_fields = ['id', 'data_inclusao']
    
    def get_caminho_imagem_url(self, obj):
        """Retorna a URL completa da imagem"""
        request = self.context.get('request')
        if obj.caminho_imagem and request:
            return request.build_absolute_uri(obj.caminho_imagem.url)
        return None
    
    def validate_caminho_imagem(self, value):
        """Valida o arquivo de imagem"""
        # Validar tamanho máximo (exemplo: 5MB)
        max_size = 5 * 1024 * 1024  # 5MB em bytes
        if value.size > max_size:
            raise serializers.ValidationError("A imagem deve ter no máximo 5MB.")
        
        # Validar tipo de arquivo
        valid_extensions = ['jpg', 'jpeg', 'png', 'webp']
        ext = value.name.split('.')[-1].lower()
        if ext not in valid_extensions:
            raise serializers.ValidationError(
                f"Formato de arquivo não suportado. Use: {', '.join(valid_extensions)}"
            )
        
        return value


class ImagemCidadeDetalheSerializer(serializers.ModelSerializer):
    """Serializer detalhado de Imagem de Cidade"""
    cidade = CidadeResumoSerializer(read_only=True)
    caminho_imagem_url = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = ImagemCidade
        fields = [
            'id',
            'caminho_imagem',
            'caminho_imagem_url',
            'data_inclusao',
            'cidade'
        ]
        read_only_fields = ['id', 'data_inclusao']
    
    def get_caminho_imagem_url(self, obj):
        """Retorna a URL completa da imagem"""
        request = self.context.get('request')
        if obj.caminho_imagem and request:
            return request.build_absolute_uri(obj.caminho_imagem.url)
        return None