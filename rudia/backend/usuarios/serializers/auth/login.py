from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from usuarios.serializers.usuario import UsuarioDetalheSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer customizado para adicionar informações extras ao token"""

    username_field = 'email'
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Adiciona informações customizadas ao token
        token['username'] = user.username
        token['email'] = user.email
        token['nome'] = user.nome
        token['tipo_usuario'] = user.tipo_usuario
        
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Adiciona informações do usuário na resposta
        data['user'] = UsuarioDetalheSerializer(
            self.user,
            context=self.context
        ).data
        
        return data


class LoginSerializer(serializers.Serializer):
    """Serializer alternativo para login simples"""
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})