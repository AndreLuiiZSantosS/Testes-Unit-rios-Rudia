from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from localizacao.models import Estado
from localizacao.serializers import EstadoSerializer, EstadoDetalheSerializer


class EstadoView(APIView):
    """
    View para listagem de estados

    GET /api/localizacao/estados/
    """
    permission_classes = [AllowAny]

    def get(self, request):
        """
        Lista todos os estados com informações básicas
        """
        try:
            # Busca todas os estados
            queryset = Estado.objects.all()

            # Serializa os dados
            serializer = EstadoSerializer(
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
                {'error': f'Erro ao listar estados: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class EstadoDetalheView(APIView):
    """
    View para detalhes de um estado específico

    GET /api/localizacao/estados/{id}/
    """
    permission_classes = [AllowAny]

    def get(self, request, id):
        """
        Retorna os detalhes de um estado pelo seu ID
        """
        try:
            # Busca o estado pelo ID
            estado = Estado.objects.get(id=id)

            # Serializa os dados
            serializer = EstadoDetalheSerializer(
                estado,
                context={'request': request}
            )

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Estado.DoesNotExist:
            return Response(
                {'error': 'Estado não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': f'Erro ao buscar estado: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )