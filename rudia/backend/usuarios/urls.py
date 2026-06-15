from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from usuarios.views import (
    RudieroRegistroView,
    ParceiroRegistroView,
    ModeradorRegistroView,
    AdministradorRegistroView,
    LoginView,
    LogoutView,
    UsuarioAtualView,
    UsuarioAtualizarView,
)

app_name = 'usuarios'

urlpatterns = [
    # Autenticação
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('auth/me/', UsuarioAtualView.as_view(), name='usuario-atual'),
    path('auth/me/update/', UsuarioAtualizarView.as_view(), name='usuario-atualizar'),

    # Registro público
    path('rudieros/registro/', RudieroRegistroView.as_view(), name='rudiero-registro'),
    path('parceiros/registro/', ParceiroRegistroView.as_view(), name='parceiro-registro'),
    
    # Registro restrito (admin)
    path('moderadores/registro/', ModeradorRegistroView.as_view(), name='moderador-registro'),
    path('administradores/registro/', AdministradorRegistroView.as_view(), name='admin-registro'),
]