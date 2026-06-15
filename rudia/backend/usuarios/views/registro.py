from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from usuarios.serializers import (
    UsuarioRegistroSerializer,
    RudieroRegistroSerializer,
    ParceiroRegistroSerializer,
    UsuarioDetalheSerializer,
    RudieroDetalheSerializer,
    ParceiroDetalheSerializer,
)
from usuarios.permissions import IsAdministrador
from usuarios.models import Usuario, Rudiero, Parceiro

class RudieroRegistroView(generics.CreateAPIView):
    """
    Endpoint público para auto-cadastro de Rudieros
    POST /api/usuarios/rudieros/registro/
    """
    queryset = Rudiero.objects.all()
    serializer_class = RudieroRegistroSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rudiero = serializer.save()
        
        return Response(
            {
                "message": "Rudiero cadastrado com sucesso!",
                "rudiero": RudieroDetalheSerializer(rudiero).data
            },
            status=status.HTTP_201_CREATED
        )

class ParceiroRegistroView(generics.CreateAPIView):
    """
    Endpoint público para cadastro de Parceiros
    POST /api/usuarios/parceiros/registro/
    """
    queryset = Parceiro.objects.all()
    serializer_class = ParceiroRegistroSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        parceiro = serializer.save()
        
        return Response(
            {
                "message": "Cadastro realizado com sucesso! Sua proposta está em análise.",
                "parceiro": ParceiroDetalheSerializer(parceiro).data
            },
            status=status.HTTP_201_CREATED
        )

class ModeradorRegistroView(generics.CreateAPIView):
    """
    Endpoint para administradores cadastrarem moderadores
    POST /api/usuarios/moderadores/registro/
    Requer: token de administrador
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioRegistroSerializer
    permission_classes = [IsAdministrador]
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['tipo_usuario'] = Usuario.TipoUsuario.MODERADOR
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        moderador = serializer.save()
        
        return Response(
            {
                "message": "Moderador cadastrado com sucesso!",
                "moderador": UsuarioDetalheSerializer(moderador).data
            },
            status=status.HTTP_201_CREATED
        )
    
class AdministradorRegistroView(generics.CreateAPIView):
    """
    Endpoint para criar outros administradores
    POST /api/usuarios/administradores/registro/
    Requer: superusuário (primeiro admin criado via createsuperuser)
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioRegistroSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied(
                "Apenas o superusuário pode criar outros administradores."
            )
        
        data = request.data.copy()
        data['tipo_usuario'] = Usuario.TipoUsuario.ADMINISTRADOR
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        admin = serializer.save()
        
        return Response(
            {
                "message": "Administrador cadastrado com sucesso!",
                "administrador": UsuarioDetalheSerializer(admin).data
            },
            status=status.HTTP_201_CREATED
        )
