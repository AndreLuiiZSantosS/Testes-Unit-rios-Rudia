from rest_framework import serializers
from django.db.models import Avg
from servicos.models import Servico
from localizacao.serializers import EnderecoSerializer, CidadeResumoSerializer
from usuarios.serializers.parceiro import ParceiroResumoSerializer
from avaliacoes.serializers.avaliacao import AvaliacaoPreviewSerializer
from .categoria import CategoriaResumoSerializer
from .tag import TagSerializer
from .horario_funcionamento import HorarioFuncionamentoSerializer


class ServicoDetalheSerializer(serializers.ModelSerializer):
    """Serializer completo para detalhes do serviço"""
    
    # Campos calculados
    preco_medio = serializers.SerializerMethodField(read_only=True)
    imagem_capa_url = serializers.SerializerMethodField(read_only=True)
    
    # Relacionamentos nested
    categoria = CategoriaResumoSerializer(read_only=True)
    cidade = CidadeResumoSerializer(read_only=True)
    parceiro = ParceiroResumoSerializer(read_only=True)
    endereco = EnderecoSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    horarios_funcionamento = serializers.SerializerMethodField(read_only=True)
    
    # Avaliações
    avaliacoes_resumo = serializers.SerializerMethodField(read_only=True)
    ultimas_avaliacoes = serializers.SerializerMethodField(read_only=True)
    
    # Links para recursos relacionados
    links = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Servico
        fields = [
            'id',
            'nome',
            'descricao',
            'capacidade_maxima',
            'preco_minimo',
            'preco_maximo',
            'preco_medio',
            'imagem_capa_url',
            'ativo',
            'data_admissao',
            'categoria',
            'cidade',
            'parceiro',
            'endereco',
            'tags',
            'horarios_funcionamento',
            'avaliacoes_resumo',
            'ultimas_avaliacoes',
            'links',
        ]
        read_only_fields = ['id', 'data_admissao']
    
    def get_preco_medio(self, obj):
        """Calcula a média entre preço mínimo e máximo"""
        if obj.preco_minimo is not None and obj.preco_maximo is not None:
            preco_medio = (obj.preco_minimo + obj.preco_maximo) / 2
            return round(float(preco_medio), 2)
        return 0
    
    def get_imagem_capa_url(self, obj):
        """Retorna URL completa da imagem de capa"""
        request = self.context.get('request')
        if obj.imagem_capa and request:
            return request.build_absolute_uri(obj.imagem_capa.url)
        return None
    
    def get_horarios_funcionamento(self, obj):
        """Retorna horários de funcionamento ordenados por dia da semana"""
        ordem_dias = {
            'SEG': 1, 'TER': 2, 'QUA': 3, 'QUI': 4,
            'SEX': 5, 'SAB': 6, 'DOM': 7
        }
        
        horarios = obj.horarios_funcionamento.all()
        horarios_ordenados = sorted(
            horarios,
            key=lambda h: ordem_dias.get(h.dia_semana, 8)
        )
        
        return HorarioFuncionamentoSerializer(
            horarios_ordenados,
            many=True,
            context=self.context
        ).data
    
    def get_avaliacoes_resumo(self, obj):
        """Retorna estatísticas completas das avaliações"""
        avaliacoes = obj.avaliacoes.all()
        
        # Calcular média geral
        media = avaliacoes.aggregate(media=Avg('nota'))['media']
        total = avaliacoes.count()
        
        # Calcular distribuição por estrelas
        distribuicao = {
            'cinco_estrelas': avaliacoes.filter(nota=5.0).count(),
            'quatro_estrelas': avaliacoes.filter(nota__gte=4.0, nota__lt=5.0).count(),
            'tres_estrelas': avaliacoes.filter(nota__gte=3.0, nota__lt=4.0).count(),
            'dois_estrelas': avaliacoes.filter(nota__gte=2.0, nota__lt=3.0).count(),
            'uma_estrela': avaliacoes.filter(nota__lt=2.0).count(),
        }
        
        return {
            'media_geral': round(media, 1) if media else 0,
            'total': total,
            'distribuicao': distribuicao
        }
    
    def get_ultimas_avaliacoes(self, obj):
        """Retorna as 3 avaliações mais recentes"""
        ultimas = obj.avaliacoes.select_related('rudiero').order_by('-data_avaliacao')[:3]
        return AvaliacaoPreviewSerializer(
            ultimas,
            many=True,
            context=self.context
        ).data
    
    def get_links(self, obj):
        """Retorna links para recursos relacionados"""
        request = self.context.get('request')
        
        links = {
            'avaliacoes': f'/api/servicos/{obj.id}/avaliacoes/',
            'categoria': f'/api/servicos/categoria/{obj.categoria.id}/',
        }
        
        # Se tiver request, gera URLs absolutas
        if request:
            base_url = request.build_absolute_uri('/').rstrip('/')
            links = {k: base_url + v for k, v in links.items()}
        
        return links
