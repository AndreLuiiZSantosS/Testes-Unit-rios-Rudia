from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from servicos.models import Tag, Categoria
from servicos.serializers.tag import TagSerializer

class TagsCategoriaView(APIView):
    """
    View para listar tags por categoria de serviço

    GET /api/servicos/categorias/{categoria_id}/tags/
    """
    permission_classes = [AllowAny]

    def get(self, request, categoria_id):
        """
        Lista todas as tags associadas a uma categoria de serviço específica
        """
        try:
            # Verifica se a categoria existe
            categoria = Categoria.objects.get(id=categoria_id)

            # Busca tags associadas à categoria via serviços
            queryset = Tag.objects.filter(
                servicos__categoria=categoria
            ).distinct()

            # Serializa os dados
            serializer = TagSerializer(
                queryset,
                many=True,
                context={'request': request}
            )

            return Response({
                'count': queryset.count(),
                'results': serializer.data
            }, status=status.HTTP_200_OK)

        except Categoria.DoesNotExist:
            return Response(
                {'error': 'Categoria não encontrada.'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': f'Erro ao listar tags: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )