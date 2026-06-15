from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from datetime import date
from usuarios.models import Rudiero

class RudieroRegistroSerializer(serializers.ModelSerializer):
    """Serializer para registro de Rudieros (auto-cadastro)"""
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
        model = Rudiero
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
            'data_nascimento',
            'genero',
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'email': {'required': True},
            'nome': {'required': True},
            'data_nascimento': {'required': True},
        }

    def validate_email(self, value):
        if Rudiero.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value
    
    def validate_data_nascimento(self, value):
        idade_minima = 13
        today = date.today()
        idade = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        
        if idade < idade_minima:
            raise serializers.ValidationError(
                f"Você deve ter no mínimo {idade_minima} anos para se cadastrar."
            )
        return value
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                "password_confirm": "As senhas não coincidem."
            })
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        
        rudiero = Rudiero.objects.create_user(
            password=password,
            **validated_data
        )

        return rudiero
    
class RudieroDetalheSerializer(serializers.ModelSerializer):
    """Serializer para visualização de detalhes do Rudiero"""
    genero_display = serializers.CharField(
        source='get_genero_display',
        read_only=True
    )
    
    class Meta:
        model = Rudiero
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
            'data_nascimento',
            'genero',
            'genero_display',
            'date_joined',
            'last_login',
        ]
        read_only_fields = ['id', 'date_joined', 'last_login']

class RudieroResumoSerializer(serializers.ModelSerializer):
    """Serializer resumido de Rudiero (para uso em nested serializers)"""
    
    class Meta:
        model = Rudiero
        fields = ['id', 'username', 'nome', 'email']
        read_only_fields = ['id']