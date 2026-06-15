from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from usuarios.serializers.auth import CustomTokenObtainPairSerializer
from usuarios.serializers import UsuarioDetalheSerializer
from usuarios.serializers import UsuarioAtualizacaoSerializer

class LoginView(TokenObtainPairView):
    """
    Endpoint para login
    POST /api/auth/login/    
    """
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]


class LogoutView(APIView):
    """
    Endpoint para logout (blacklist do refresh token)
    POST /api/auth/logout/
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token é obrigatório"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(
                {"message": "Logout realizado com sucesso"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class UsuarioAtualView(APIView):
    """
    Endpoint para obter dados do usuário autenticado
    GET /api/auth/me/
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = UsuarioDetalheSerializer(request.user)
        return Response({"user": serializer.data})


class UsuarioAtualizarView(APIView):
    """
    Endpoint para atualizar dados do usuário autenticado
    PATCH /api/auth/me/update/
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def patch(self, request):
        usuario = request.user
            
        serializer = UsuarioAtualizacaoSerializer(usuario, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response_serializer = UsuarioDetalheSerializer(usuario)
            return Response({"user": response_serializer.data}, status=status.HTTP_200_OK)
            
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    