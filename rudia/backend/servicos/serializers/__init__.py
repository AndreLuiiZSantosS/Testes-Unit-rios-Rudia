from .servico_lista import ServicoListaSerializer
from .servico_detalhe import ServicoDetalheSerializer
from .servico_create import ServicoCreateSerializer
from .servico_resumo import ServicoResumoSerializer
from .categoria import CategoriaSerializer, CategoriaResumoSerializer
from .tag import TagSerializer
from .horario_funcionamento import HorarioFuncionamentoSerializer

__all__ = [
    'ServicoListaSerializer',
    'ServicoDetalheSerializer',
    'ServicoCreateSerializer',
    'ServicoResumoSerializer',
    'CategoriaSerializer',
    'CategoriaResumoSerializer',
    'TagSerializer',
    'HorarioFuncionamentoSerializer',
]
