from rest_framework import permissions


class IsRudieroOrReadOnly(permissions.BasePermission):
    """
    Permissão customizada para viagens:
    - GET, HEAD, OPTIONS: Permitido para todos
    - POST, PUT, PATCH, DELETE: Apenas para usuários Rudiero autenticados
    """
    
    def has_permission(self, request, view):
        # Métodos seguros (leitura) permitidos para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Métodos de escrita apenas para Rudiero autenticado
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.tipo_usuario == 'RUDIERO'
        )


class IsRudieroOwner(permissions.BasePermission):
    """
    Permissão para garantir que apenas o Rudiero dono da viagem pode editá-la/deletá-la
    """
    
    def has_object_permission(self, request, view, obj):
        # Leitura permitida para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Escrita apenas se for o dono da viagem
        return (
            request.user.is_authenticated and 
            obj.rudiero.usuario_ptr_id == request.user.id
        )