from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Prefetch
from viagem.models import Viagem
from viagem.serializers.viagem_create import ViagemCreateSerializer
from viagem.serializers.viagem_detalhe import ViagemDetalheSerializer
from viagem.permissions import IsRudieroOrReadOnly
from rest_framework.permissions import IsAuthenticated
from servicos.models import Servico


class ViagemView(APIView):
    """
    View para criação de viagens
    
    POST /api/viagens/
    """
    permission_classes = [IsRudieroOrReadOnly]
    
    def post(self, request):
        """
        Cria uma nova viagem
        
        Requer autenticação como RUDIERO
        """
        serializer = ViagemCreateSerializer(
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            try:
                viagem = serializer.save()
                
                viagem_completa = Viagem.objects.select_related(
                    'rudiero',
                    'cidade_destino',
                    'cidade_destino__estado'
                ).prefetch_related(
                    Prefetch(
                        'servicos',
                        queryset=Servico.objects.select_related(
                            'categoria',
                            'parceiro'
                        )
                    )
                ).get(id=viagem.id)
                
                response_serializer = ViagemDetalheSerializer(
                    viagem_completa,
                    context={'request': request}
                )
                
                return Response(
                    {
                        'viagem': response_serializer.data,
                        'mensagem': 'Viagem criada com sucesso!'
                    },
                    status=status.HTTP_201_CREATED
                )
                
            except Exception as e:
                return Response(
                    {'error': f'Erro ao criar viagem: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ViagemDetalheView(APIView):
    """
    View para retornar os dados de uma viagem específica
    
    GET /api/viagens/{viagem_id}
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, viagem_id):
        """
        Retorna detalhes completos de uma viagem específica
        Path Parameters:
        - viagem_id: ID da viagem
        """
        try:
            try:
                viagem_id = int(viagem_id)
            except (ValueError, TypeError):
                return Response(
                    {'error': 'O ID da viagem deve ser um número inteiro'},
                    status = status.HTTP_400_BAD_REQUEST
                )
            try:
                viagem = Viagem.objects.get(id=viagem_id)
            except:
                return Response(
                    {'error': 'Viagem não encontrada'},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = ViagemDetalheSerializer(viagem)
            return Response({'viagem': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': f'Erro ao buscar viagem: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


