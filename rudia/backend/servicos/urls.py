from django.urls import path
from .views import (
    ServicoView,
    ServicoCategoriasListView,
    ServicoDetalheView,
    ServicoAvaliacoesView,
    CategoriaView,
    TagsCategoriaView
)

app_name = 'servicos'

urlpatterns = [
    path('', ServicoView.as_view(), name='servico-list'),
    path('categoria/<int:categoria_id>/', ServicoCategoriasListView.as_view(), name='servico-categoria-list'),
    path('<int:servico_id>/', ServicoDetalheView.as_view(), name='servico-detalhe'),
    path('<int:servico_id>/avaliacoes/', ServicoAvaliacoesView.as_view(), name='servico-avaliacoes'),
    path('categorias/<int:categoria_id>/tags/', TagsCategoriaView.as_view(), name='tags-categoria'),
    path('categorias/', CategoriaView.as_view(), name='categoria-list'),
]
