from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Count
from localizacao.models import Cidade
from localizacao.serializers import CidadeListaSerializer


class CidadeView(APIView):
    """
    View para listagem de cidades
    
    GET /api/localizacao/cidades/
    """
    permission_classes = [AllowAny]
    
    def get(self, request):
        """
        Lista todas as cidades com informações básicas
        
        Query parameters opcionais:
        - estado: Filtrar por ID do estado
        - estado_sigla: Filtrar por sigla do estado (ex: SP, RJ)
        - nome: Buscar cidades por nome (case-insensitive, parcial)
        """
        try:
            # Busca base com anotações para otimização
            queryset = Cidade.objects.select_related('estado').annotate(
                total_imagens=Count('imagens')
            )
            
            # Filtros opcionais
            estado_id = request.query_params.get('estado')
            estado_sigla = request.query_params.get('estado_sigla')
            nome = request.query_params.get('nome')
            
            if estado_id:
                queryset = queryset.filter(estado_id=estado_id)
            
            if estado_sigla:
                queryset = queryset.filter(estado__sigla__iexact=estado_sigla)
            
            if nome:
                queryset = queryset.filter(nome__icontains=nome)
            
            # Serializa os dados
            serializer = CidadeListaSerializer(
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
                {
                    'error': 'Erro ao buscar cidades',
                    'detail': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
