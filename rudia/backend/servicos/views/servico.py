from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models import Avg, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from servicos.models import Servico, Categoria
from servicos.serializers import ServicoListaSerializer, ServicoDetalheSerializer, ServicoCreateSerializer
from servicos.permissions import IsParceiroOrReadOnly
from avaliacoes.serializers import AvaliacaoSerializer


class ServicoView(APIView):
    """
    View para listagem e criação de serviços
    
    GET /api/servicos/
    GET /api/servicos/?page=2&size=20
    POST /api/servicos/
    """
    permission_classes = [IsParceiroOrReadOnly]
    
    def get(self, request):
        """
        Lista todos os serviços ativos
        
        Query Parameters:
        - page: Número da página (padrão: 1)
        - size: Quantidade de itens por página (padrão: 10)
        """
        try:
            page = request.query_params.get('page', 1)
            size = request.query_params.get('size', 10)
            
            try:
                page = int(page)
                if page < 1:
                    page = 1
            except (ValueError, TypeError):
                page = 1
            
            try:
                size = int(size)
                if size < 1:
                    size = 10
                elif size > 100:  
                    size = 100
            except (ValueError, TypeError):
                size = 10
            
            # Buscar serviços ativos com otimizações
            queryset = Servico.objects.filter(
                ativo=True
            ).select_related(
                'categoria',
                'cidade',
                'cidade__estado',
                'parceiro'
            ).annotate(
                avaliacao_geral=Avg('avaliacoes__nota')
            ).order_by('-data_admissao')
            
            # Aplicar paginação
            paginator = Paginator(queryset, size)
            
            try:
                servicos_page = paginator.page(page)
            except PageNotAnInteger:
                servicos_page = paginator.page(1)
            except EmptyPage:
                servicos_page = paginator.page(paginator.num_pages)
            
            serializer = ServicoListaSerializer(
                servicos_page,
                many=True,
                context={'request': request}
            )
            
            response_data = {
                'paginacao': {
                    'page': servicos_page.number,
                    'size': size,
                    'total_pages': paginator.num_pages,
                    'total_items': paginator.count,
                    'has_next': servicos_page.has_next(),
                    'has_previous': servicos_page.has_previous(),
                    'next_page': servicos_page.next_page_number() if servicos_page.has_next() else None,
                    'previous_page': servicos_page.previous_page_number() if servicos_page.has_previous() else None,
                },
                'servicos': serializer.data
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Erro ao buscar serviços: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        """
        Cria um novo serviço
        
        Requer autenticação como PARCEIRO
        O serviço é criado com status PENDENTE até ser aprovado por um moderador
        """
        serializer = ServicoCreateSerializer(
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            try:
                servico = serializer.save()
                
                # Retorna os dados completos do serviço criado
                response_serializer = ServicoDetalheSerializer(
                    servico,
                    context={'request': request}
                )
                
                return Response(
                    response_serializer.data,
                    status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(
                    {'error': f'Erro ao criar serviço: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ServicoCategoriasListView(APIView):
    """
    View para listagem de serviços por categoria
    
    GET /api/servicos/categoria/{categoria_id}/
    GET /api/servicos/categoria/{categoria_id}/?destino=5&viajantes=4&page=1&size=10
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, categoria_id):
        """
        Lista serviços filtrados por categoria
        
        Path Parameters:
        - categoria_id: ID da categoria (ex: 1, 2, 3)
        
        Query Parameters:
        - destino: ID da cidade destino (opcional)
        - viajantes: Número de viajantes (filtra por capacidade_maxima >= viajantes) (opcional)
        - page: Número da página (padrão: 1)
        - size: Quantidade de itens por página (padrão: 10)
        """
        try:
            try:
                categoria_id = int(categoria_id)
            except (ValueError, TypeError):
                return Response(
                    {'error': 'O ID da categoria deve ser um número inteiro.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            try:
                categoria = Categoria.objects.get(id=categoria_id)
            except Categoria.DoesNotExist:
                return Response(
                    {'error': f'Categoria com id {categoria_id} não encontrada.'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            destino = request.query_params.get('destino')
            viajantes = request.query_params.get('viajantes')
            page = request.query_params.get('page', 1)
            size = request.query_params.get('size', 10)
            
            try:
                page = int(page)
                if page < 1:
                    page = 1
            except (ValueError, TypeError):
                page = 1
            
            try:
                size = int(size)
                if size < 1:
                    size = 10
                elif size > 100:
                    size = 100
            except (ValueError, TypeError):
                size = 10
            
            # Query base: serviços ativos da categoria
            queryset = Servico.objects.filter(
                ativo=True,
                categoria_id=categoria_id
            ).select_related(
                'categoria',
                'cidade',
                'cidade__estado',
                'parceiro'
            ).annotate(
                avaliacao_geral=Avg('avaliacoes__nota')
            )
            
            if destino:
                try:
                    destino_id = int(destino)
                    queryset = queryset.filter(cidade__id=destino_id)
                except ValueError:
                    return Response(
                        {'error': 'O parâmetro "destino" deve ser um número inteiro.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            if viajantes:
                try:
                    num_viajantes = int(viajantes)
                    if num_viajantes > 0:
                        queryset = queryset.filter(capacidade_maxima__gte=num_viajantes)
                except ValueError:
                    return Response(
                        {'error': 'O parâmetro "viajantes" deve ser um número inteiro positivo.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            # Ordenar por avaliação e data de admissão
            queryset = queryset.order_by('-avaliacao_geral', '-data_admissao')
            
            # Verificar se existem resultados
            total_resultados = queryset.count()
            
            # Aplicar paginação
            paginator = Paginator(queryset, size)
            
            try:
                servicos_page = paginator.page(page)
            except PageNotAnInteger:
                servicos_page = paginator.page(1)
            except EmptyPage:
                servicos_page = paginator.page(paginator.num_pages if paginator.num_pages > 0 else 1)
            
            serializer = ServicoListaSerializer(
                servicos_page,
                many=True,
                context={'request': request}
            )
            
            response_data = {
                'categoria': {
                    'id': categoria.id,
                    'nome': categoria.nome
                },
                'filtros_aplicados': {
                    'destino': int(destino) if destino else None,
                    'viajantes': int(viajantes) if viajantes else None,
                },
                'paginacao': {
                    'page': servicos_page.number,
                    'size': size,
                    'total_pages': paginator.num_pages,
                    'total_items': total_resultados,
                    'has_next': servicos_page.has_next(),
                    'has_previous': servicos_page.has_previous(),
                    'next_page': servicos_page.next_page_number() if servicos_page.has_next() else None,
                    'previous_page': servicos_page.previous_page_number() if servicos_page.has_previous() else None,
                },
                'servicos': serializer.data
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Erro ao buscar serviços: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ServicoDetalheView(APIView):
    """
    View para detalhes completos de um serviço
    
    GET /api/servicos/{servico_id}/
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, servico_id):
        """
        Retorna detalhes completos de um serviço específico
        
        Path Parameters:
        - servico_id: ID do serviço
        """
        try:
            # Validar que servico_id é um número inteiro
            try:
                servico_id = int(servico_id)
            except (ValueError, TypeError):
                return Response(
                    {'error': 'O ID do serviço deve ser um número inteiro.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Buscar serviço com otimizações
            try:
                servico = Servico.objects.select_related(
                    'categoria',
                    'cidade',
                    'cidade__estado',
                    'parceiro',
                    'endereco'
                ).prefetch_related(
                    'tags',
                    'horarios_funcionamento',
                    'avaliacoes',
                    'avaliacoes__rudiero'
                ).get(id=servico_id)
            except Servico.DoesNotExist:
                return Response(
                    {'error': f'Serviço com id {servico_id} não encontrado.'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Verificar se serviço está ativo
            if not servico.ativo:
                return Response(
                    {'error': 'Este serviço não está disponível no momento.'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Serializar dados
            serializer = ServicoDetalheSerializer(servico, context={'request': request})
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Erro ao buscar serviço: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ServicoAvaliacoesView(APIView):
    """
    View para listar avaliações de um serviço específico
    
    GET /api/servicos/{servico_id}/avaliacoes/
    GET /api/servicos/{servico_id}/avaliacoes/?page=2&size=10
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, servico_id):
        """
        Lista avaliações de um serviço específico
        
        Path Parameters:
        - servico_id: ID do serviço
        
        Query Parameters:
        - page: Número da página (padrão: 1)
        - size: Quantidade de itens por página (padrão: 5)
        """
        try:
            # Validar que servico_id é um número inteiro
            try:
                servico_id = int(servico_id)
            except (ValueError, TypeError):
                return Response(
                    {'error': 'O ID do serviço deve ser um número inteiro.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Verificar se o serviço existe
            try:
                servico = Servico.objects.only('id', 'nome').get(id=servico_id)
            except Servico.DoesNotExist:
                return Response(
                    {'error': f'Serviço com id {servico_id} não encontrado.'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Obter parâmetros de paginação
            page = request.query_params.get('page', 1)
            size = request.query_params.get('size', 5)
            
            # Validar parâmetros de paginação
            try:
                page = int(page)
                if page < 1:
                    page = 1
            except (ValueError, TypeError):
                page = 1
            
            try:
                size = int(size)
                if size < 1:
                    size = 5
                elif size > 100:
                    size = 100
            except (ValueError, TypeError):
                size = 5
            
            # Buscar avaliações do serviço
            avaliacoes_queryset = servico.avaliacoes.select_related(
                'rudiero'
            ).order_by('-data_avaliacao')
            
            # Calcular estatísticas
            stats = avaliacoes_queryset.aggregate(
                media_geral=Avg('nota'),
                total=Count('id')
            )
            
            # Aplicar paginação
            paginator = Paginator(avaliacoes_queryset, size)
            
            try:
                avaliacoes_page = paginator.page(page)
            except PageNotAnInteger:
                avaliacoes_page = paginator.page(1)
            except EmptyPage:
                avaliacoes_page = paginator.page(paginator.num_pages if paginator.num_pages > 0 else 1)
            
            # Serializar dados
            serializer = AvaliacaoSerializer(
                avaliacoes_page,
                many=True,
                context={'request': request}
            )
            
            # Montar resposta
            response_data = {
                'servico': {
                    'id': servico.id,
                    'nome': servico.nome
                },
                'estatisticas': {
                    'media_geral': round(stats['media_geral'], 1) if stats['media_geral'] else 0,
                    'total': stats['total']
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
