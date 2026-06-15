from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from avaliacoes.models import Avaliacao
from avaliacoes.serializers import AvaliacaoSerializer


class AvaliacaoListView(APIView):
    """
    View para listar avaliações de um serviço ou roteiro específico
    
    GET /api/avaliacoes/?tipo=servico&objeto_id=1
    GET /api/avaliacoes/?tipo=roteiro&objeto_id=5&page=2&size=10
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        """
        Lista todas as avaliações de um serviço ou roteiro específico
        
        Query Parameters:
        - tipo: 'servico' ou 'roteiro' (obrigatório)
        - objeto_id: ID do serviço ou roteiro (obrigatório)
        - page: Número da página (padrão: 1)
        - size: Quantidade de itens por página (padrão: 5)
        """
        try:
            # Obter parâmetros da query string
            tipo_objeto = request.query_params.get('tipo')
            objeto_id = request.query_params.get('objeto_id')
            page = request.query_params.get('page', 1)
            size = request.query_params.get('size', 5)
            
            # Validar parâmetros obrigatórios
            if not tipo_objeto or not objeto_id:
                return Response(
                    {
                        'error': 'Os parâmetros "tipo" e "objeto_id" são obrigatórios.',
                        'exemplo': '/api/avaliacoes/?tipo=servico&objeto_id=1'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validar tipo de objeto
            tipo_objeto = tipo_objeto.lower()
            if tipo_objeto not in ['servico', 'roteiro']:
                return Response(
                    {
                        'error': 'O parâmetro "tipo" deve ser "servico" ou "roteiro".'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validar que objeto_id é um número
            try:
                objeto_id = int(objeto_id)
            except ValueError:
                return Response(
                    {'error': 'O parâmetro "objeto_id" deve ser um número inteiro.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validar parâmetros de paginação (usa valores padrão se inválidos)
            try:
                page = int(page)
                if page < 1:
                    page = 1
            except (ValueError, TypeError):
                page = 1  # Valor padrão
            
            try:
                size = int(size)
                if size < 1:
                    size = 5  # Valor padrão
                elif size > 100:  # Limite máximo de itens por página
                    size = 100
            except (ValueError, TypeError):
                size = 5  # Valor padrão
            
            # Obter o ContentType do modelo
            try:
                if tipo_objeto == 'servico':
                    content_type = ContentType.objects.get(app_label='servicos', model='servico')
                else:  # roteiro
                    content_type = ContentType.objects.get(app_label='viagem', model='roteiro')
            except ContentType.DoesNotExist:
                return Response(
                    {'error': f'Tipo de objeto "{tipo_objeto}" não encontrado.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Verificar se o objeto existe
            model_class = content_type.model_class()
            if not model_class.objects.filter(pk=objeto_id).exists():
                return Response(
                    {
                        'error': f'{tipo_objeto.title()} com id {objeto_id} não encontrado.'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Buscar avaliações
            avaliacoes_queryset = Avaliacao.objects.filter(
                content_type=content_type,
                object_id=objeto_id
            ).select_related('rudiero').order_by('-data_avaliacao')
            
            # Calcular estatísticas (do total, não da página)
            stats = avaliacoes_queryset.aggregate(
                media_nota=Avg('nota'),
                total_avaliacoes=Count('id')
            )
            
            # Aplicar paginação
            paginator = Paginator(avaliacoes_queryset, size)
            
            try:
                avaliacoes_page = paginator.page(page)
            except PageNotAnInteger:
                avaliacoes_page = paginator.page(1)
            except EmptyPage:
                avaliacoes_page = paginator.page(paginator.num_pages)
            
            # Serializar dados da página atual
            serializer = AvaliacaoSerializer(
                avaliacoes_page, 
                many=True,
                context={'request': request}
            )
            
            # Montar resposta
            response_data = {
                'tipo_objeto': tipo_objeto,
                'objeto_id': objeto_id,
                'estatisticas': {
                    'media_nota': round(stats['media_nota'], 1) if stats['media_nota'] else 0,
                    'total_avaliacoes': stats['total_avaliacoes']
                },
                'paginacao': {
                    'page': avaliacoes_page.number,
                    'size': size,
                    'total_pages': paginator.num_pages,
                    'total_items': paginator.count,
                    'has_next': avaliacoes_page.has_next(),
                    'has_previous': avaliacoes_page.has_previous(),
                    'next_page': avaliacoes_page.next_page_number() if avaliacoes_page.has_next() else None,
                    'previous_page': avaliacoes_page.previous_page_number() if avaliacoes_page.has_previous() else None,
                },
                'avaliacoes': serializer.data
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Erro ao buscar avaliações: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )