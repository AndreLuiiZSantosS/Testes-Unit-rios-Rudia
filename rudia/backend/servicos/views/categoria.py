from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from servicos.models import Categoria
from servicos.serializers.categoria import CategoriaSerializer

class CategoriaView(APIView):
    """
    View para listagem de categorias de serviços
    
    GET /api/servicos/categorias/
    """
    permission_classes = [AllowAny]
    
    def get(self, request):
        """
        Lista todas as categorias de serviços disponíveis
        """
        try:
            # Busca todas as categorias
            queryset = Categoria.objects.all()
            
            # Serializa os dados
            serializer = CategoriaSerializer(
                queryset,
                many=True,
                context={'request': request}
            )
            
            return Response({
                'count': queryset.count(),
                'results': serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Erro ao listar categorias: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )