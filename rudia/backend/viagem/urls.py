from django.urls import path
from .views import ViagemView, ViagemDetalheView

app_name = 'viagem'

urlpatterns = [
    path('', ViagemView.as_view(), name='viagem-create'),
    path('<int:viagem_id>/', ViagemDetalheView.as_view(), name='viagem-detalhe')
]