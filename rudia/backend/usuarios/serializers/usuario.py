from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from usuarios.models import Usuario

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    """Serializer para registro de usuários (Administrador ou Moderador)"""
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
        model = Usuario
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
            'tipo_usuario',
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'email': {'required': True},
            'nome': {'required': True},
            'tipo_usuario': {
                'required': True,
                'help_text': 'Tipo de usuário: MODERADOR ou ADMINISTRADOR'
            }
        }

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value
    
    def validate_tipo_usuario(self, value):
        """Valida que apenas MODERADOR ou ADMINISTRADOR podem ser criados por este serializer"""
        if value not in [Usuario.TipoUsuario.MODERADOR, Usuario.TipoUsuario.ADMINISTRADOR]:
            raise serializers.ValidationError(
                "Este endpoint só permite criar usuários do tipo MODERADOR ou ADMINISTRADOR."
            )
        return value
    
    def validate(self, attrs):
        """Valida que as senhas coincidem"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                "password_confirm": "As senhas não coincidem."
            })
        return attrs
    
    def create(self, validated_data):
        """Cria um novo usuário"""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        
        usuario = Usuario.objects.create_user(
            password=password,
            **validated_data
        )

        return usuario
    
class UsuarioDetalheSerializer(serializers.ModelSerializer):
    """Serializer para visualização de detalhes do usuário"""
    tipo_usuario_display = serializers.CharField(
        source='get_tipo_usuario_display',
        read_only=True
    )
    
    class Meta:
        model = Usuario
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
            'tipo_usuario',
            'tipo_usuario_display',
            'date_joined',
            'last_login',
        ]
        read_only_fields = ['id', 'date_joined', 'last_login', 'tipo_usuario']

class UsuarioAtualizacaoSerializer(serializers.ModelSerializer):
    """Serializer para atualização de dados do usuário (Parceiro/Rudiero)"""
    class Meta:
        model = Usuario
        fields = [
            'telefone',
            'foto_perfil',
            'url_instagram',
            'url_facebook',
            'url_x',
            'url_tiktok',
        ]