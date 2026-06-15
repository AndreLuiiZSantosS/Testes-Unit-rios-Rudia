from django.urls import path
from .views import CidadeView, EstadoView, EstadoDetalheView

app_name = 'localizacao'

urlpatterns = [
    path('cidades/', CidadeView.as_view(), name='cidade-lista'),
    path('estados/', EstadoView.as_view(), name='estado-lista'),
    path('estados/<int:id>/', EstadoDetalheView.as_view(), name='estado-detalhe'),
]
