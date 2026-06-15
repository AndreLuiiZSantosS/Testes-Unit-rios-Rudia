from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from moderacao.models import Proposta
from usuarios.models import Parceiro
import re

class ParceiroRegistroSerializer(serializers.ModelSerializer):
    """Serializer para registro de Parceiros com proposta automática"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    
    class Meta:
        model = Parceiro
        fields = [
            'id',
            'username',
            'email',
            'password',
            'password_confirm',
            'nome',
            'telefone',
            'foto_perfil',
            'url_instagram',
            'url_facebook',
            'url_x',
            'url_tiktok',
            'cnpj',
            'ativo',
        ]
        read_only_fields = ['id', 'ativo']
        extra_kwargs = {
            'email': {'required': True},
            'nome': {'required': True},
            'cnpj': {'required': True},
        }

    def validate_email(self, value):
        if Parceiro.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value
    
    def validate_cnpj(self, value):
        """Valida formato do CNPJ (apenas números, 14 dígitos)"""
        cnpj_numeros = re.sub(r'\D', '', value)
        
        if len(cnpj_numeros) != 14:
            raise serializers.ValidationError("CNPJ deve conter 14 dígitos.")
        
        return cnpj_numeros
    
    def validate(self, attrs):
        """Valida que as senhas coincidem"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                "password_confirm": "As senhas não coincidem."
            })
        return attrs
    
    def create(self, validated_data):
        """Cria um novo Parceiro e gera proposta para análise"""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        validated_data['ativo'] = False
        
        parceiro = Parceiro.objects.create_user(
            password=password,
            **validated_data
        )

        Proposta.objects.create(content_object=parceiro)
        
        return parceiro
    
class ParceiroDetalheSerializer(serializers.ModelSerializer):
    """Serializer para visualização de detalhes do Parceiro"""
    proposta_status = serializers.SerializerMethodField()
    
    class Meta:
        model = Parceiro
        fields = [
            'id',
            'username',
            'email',
            'nome',
            'telefone',
            'foto_perfil',
            'url_instagram',
            'url_facebook',
            'url_x',
            'url_tiktok',
            'cnpj',
            'ativo',
            'data_admissao',
            'proposta_status',
            'date_joined',
            'last_login',
        ]
        read_only_fields = ['id', 'ativo', 'data_admissao', 'date_joined', 'last_login']
    
    def get_proposta_status(self, obj):
        """Retorna o status da proposta mais recente"""
        proposta = obj.propostas.order_by('-data_criacao').first()
        if proposta:
            return {
                'status': proposta.get_status_proposta_display(),
                'data_criacao': proposta.data_criacao,
                'comentario_moderador': proposta.comentario_moderador,
            }
        return None


class ParceiroResumoSerializer(serializers.Serializer):
    """Serializer resumido de Parceiro (para nested)"""
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    nome_fantasia = serializers.CharField(read_only=True)
    foto_perfil = serializers.SerializerMethodField(read_only=True)
    
    def get_foto_perfil(self, obj):
        """Retorna URL completa da foto de perfil"""
        request = self.context.get('request')
        if obj.foto_perfil and request:
            return request.build_absolute_uri(obj.foto_perfil.url)
        return None
