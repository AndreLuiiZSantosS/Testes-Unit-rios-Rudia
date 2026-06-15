from django.urls import path
from .views import AvaliacaoListView

app_name = 'avaliacoes'

urlpatterns = [
    path('', AvaliacaoListView.as_view(), name='avaliacao-list'),
]